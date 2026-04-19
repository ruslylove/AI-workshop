#!/usr/bin/env python3
"""
generate_memo.py – สร้างบันทึกข้อความ ภาควิชา ECE KMUTNB
จาก JSON config โดยใช้ template ของภาควิชา

Usage:
    python generate_memo.py --config memo.json --output result.docx

Config schema (memo.json):
{
  "เรื่อง": "...",
  "ที่": "อว ๗๑๕๖.๐๑/___",          // optional, default blank
  "วันที่": "19 เมษายน 2569",          // optional, default today
  "ลงนาม": {
    "ชื่อ": "ผู้ช่วยศาสตราจารย์ ดร.รุสลี่ สุทธวีร์กูล",
    "ตำแหน่ง": "อาจารย์ประจำภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์",
    "โทร": "0-2555-2000 ต่อ 8519"     // optional
  },
  "เนื้อหา": [
    {
      "type": "paragraph",
      "indent": true,                  // first-line indent (ด้วย / เนื่องจาก)
      "text": "ด้วย ..."
    },
    {
      "type": "paragraph",
      "indent": true,
      "text": "..."
    },
    {
      "type": "list_intro",           // paragraph before a list
      "indent": true,
      "text": "... มีดังนี้"
    },
    {
      "type": "numbered_list",
      "items": ["item 1", "item 2"]
    },
    {
      "type": "detail_list",          // label: value pairs
      "items": [
        {"label": "ชื่อโครงการ", "value": "..."},
        {"label": "งบประมาณ",    "value": "50,000 บาท"}
      ]
    }
  ],
  "เอกสารแนบ": [                      // optional
    "ข้อ 1 ...",
    "ข้อ 2 ..."
  ]
}
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date

# ──────────────────────────────────────────────────────────────
# XML helpers
# ──────────────────────────────────────────────────────────────
FONT_RUN = ('TH Sarabun New', 'TH Sarabun New', 'TH Sarabun New')

RPR = '<w:rPr><w:rFonts w:ascii="TH Sarabun New" w:hAnsi="TH Sarabun New" w:cs="TH Sarabun New"/><w:cs/></w:rPr>'
RPR_BOLD = '<w:rPr><w:rFonts w:ascii="TH Sarabun New" w:hAnsi="TH Sarabun New" w:cs="TH Sarabun New"/><w:b/><w:bCs/><w:cs/></w:rPr>'
PPR_DIST = ('<w:pPr><w:ind w:right="-46"/><w:jc w:val="thaiDistribute"/>'
            '<w:rPr><w:rFonts w:ascii="TH Sarabun New" w:hAnsi="TH Sarabun New" w:cs="TH Sarabun New"/></w:rPr></w:pPr>')

_pid_counter = [0xAA0100]

def next_pid():
    _pid_counter[0] += 1
    return f'{_pid_counter[0]:08X}'

def esc(text: str) -> str:
    """Escape XML special characters."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))

def run(text: str, bold=False) -> str:
    rp = RPR_BOLD if bold else RPR
    return f'<w:r>{rp}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'

def tabs(n=2) -> str:
    return f'<w:r>{RPR}' + '<w:tab/>' * n + '</w:r>'

def para_dist(inner: str, pid: str = None) -> str:
    pid = pid or next_pid()
    return (f'<w:p w14:paraId="{pid}" w14:textId="77777777" '
            f'w:rsidR="00BB0001" w:rsidRDefault="00BB0001" w:rsidP="00844053">'
            f'\n      {PPR_DIST}\n      {inner}\n    </w:p>\n    ')

def blank_para() -> str:
    return para_dist('')

# ──────────────────────────────────────────────────────────────
# Body paragraph builders
# ──────────────────────────────────────────────────────────────

def build_paragraph(text: str, indent: bool = True) -> str:
    inner = (tabs(2) if indent else '') + run(text)
    return para_dist(inner)

def build_numbered_list(items: list) -> str:
    out = ''
    for i, item in enumerate(items, 1):
        inner = tabs(2) + run(f'{i}. {item}')
        out += para_dist(inner)
    return out

def build_detail_list(items: list) -> str:
    out = ''
    for item in items:
        lbl = item.get('label', '')
        val = item.get('value', '')
        inner = tabs(2) + run('        - ') + run(f'{lbl}  ', bold=True) + run(val)
        out += para_dist(inner)
    return out

def build_body(content: list) -> str:
    parts = []
    for block in content:
        btype = block.get('type', 'paragraph')
        if btype == 'paragraph':
            parts.append(build_paragraph(
                block.get('text', ''),
                indent=block.get('indent', True)
            ))
            parts.append(blank_para())
        elif btype == 'list_intro':
            parts.append(build_paragraph(
                block.get('text', ''),
                indent=block.get('indent', True)
            ))
        elif btype == 'numbered_list':
            parts.append(build_numbered_list(block.get('items', [])))
            parts.append(blank_para())
        elif btype == 'detail_list':
            parts.append(build_detail_list(block.get('items', [])))
            parts.append(blank_para())
    return ''.join(parts)

# ──────────────────────────────────────────────────────────────
# Attachment section builder
# ──────────────────────────────────────────────────────────────

def build_attachments(items: list) -> str:
    if not items:
        return ''
    out = para_dist(run('เอกสารแนบ'))
    for i, item in enumerate(items, 1):
        out += para_dist(run(f'{i}. {item}'))
    return out

# ──────────────────────────────────────────────────────────────
# Main replacements on document.xml
# ──────────────────────────────────────────────────────────────
# These paraId values are stable in the ECE department template.
PARA_SUBJECT_START = '16DEE251'     # paragraph containing เรื่อง label
PARA_BODY_FIRST    = '4168ED9B'     # first body paragraph (after เรียน blank)
PARA_JUENRIAN      = '56B6A4BF'     # จึงเรียนมาเพื่อโปรดพิจารณาอนุมัติ
PARA_SIG_TITLE     = '6E823166'     # paragraph with position title
PARA_ATTACH_HDR    = '5FEDAEB4'     # เอกสารแนบ header paragraph


def replace_subject(xml: str, subject: str) -> str:
    """Replace text inside the เรื่อง paragraph."""
    # Pattern: find the last <w:t> run(s) after the เรื่อง bold label
    # The paragraph (16DEE251) ends with a run containing the subject text.
    # We replace whatever is between '  ' spacing run and end of </w:p>
    pattern = r'(w14:paraId="16DEE251".*?<w:b/><w:bCs/>.*?</w:r>)(.*?)(</w:p>)'
    # Simpler: just replace the known subject text string
    # Find current subject text (the last <w:t> in the paragraph)
    para_start = xml.find(f'w14:paraId="{PARA_SUBJECT_START}"')
    para_end   = xml.find('</w:p>', para_start) + 6
    para_xml   = xml[para_start:para_end]

    # Remove all existing <w:t> runs after the bold เรื่อง run
    # Strategy: keep everything up to end of last shape/drawing + bold label run,
    # then replace trailing text runs
    bold_end = para_xml.rfind('</w:r>', 0, para_xml.find(f'<w:t>{esc("เรื่อง")}</w:t>') + 50)
    # Find index of เรื่อง text node
    subject_label_pos = para_xml.find('<w:t>เรื่อง</w:t>')
    if subject_label_pos == -1:
        subject_label_pos = para_xml.find('<w:t xml:space="preserve">เรื่อง</w:t>')

    run_end_after_label = para_xml.find('</w:r>', subject_label_pos) + 6

    # Everything from run_end_after_label to </w:p> = old subject runs
    new_subject_run = (
        f'\n      <w:r>{RPR}<w:t xml:space="preserve">  </w:t></w:r>'
        f'\n      {run(subject)}'
        f'\n    '
    )
    new_para = para_xml[:run_end_after_label] + new_subject_run + '</w:p>'
    return xml[:para_start] + new_para + xml[para_end:]


def replace_body(xml: str, body_xml: str) -> str:
    """Replace paragraphs from PARA_BODY_FIRST up to (not including) PARA_JUENRIAN."""
    start_attr = xml.find(f'w14:paraId="{PARA_BODY_FIRST}"')
    end_attr   = xml.find(f'w14:paraId="{PARA_JUENRIAN}"')
    if start_attr == -1 or end_attr == -1:
        raise ValueError(f'Body anchor paraIds not found in template XML. '
                         f'First={start_attr}, Last={end_attr}')
    # Back up to the opening <w:p tag of each paragraph
    start = xml.rfind('<w:p ', 0, start_attr)
    end   = xml.rfind('<w:p ', 0, end_attr)   # include <w:p of จึงเรียน paragraph
    return xml[:start] + body_xml + xml[end:]


def replace_sig_title(xml: str, title: str) -> str:
    """Replace position title in the signature block."""
    para_start = xml.find(f'w14:paraId="{PARA_SIG_TITLE}"')
    para_end   = xml.find('</w:p>', para_start) + 6

    spaces = '                     '  # preserve original indentation spaces
    new_para_xml = (
        f'<w:p w14:paraId="{PARA_SIG_TITLE}" w14:textId="77777777" '
        f'w:rsidR="009D175D" w:rsidRDefault="009D175D" w:rsidP="001C1843">\n'
        f'      <w:pPr><w:ind w:right="-46"/><w:jc w:val="thaiDistribute"/>'
        f'<w:rPr><w:rFonts w:ascii="TH Sarabun New" w:hAnsi="TH Sarabun New" w:cs="TH Sarabun New"/></w:rPr></w:pPr>\n'
        f'      <w:r>{RPR}<w:tab/><w:tab/><w:tab/><w:tab/></w:r>\n'
        f'      <w:r>{RPR}<w:t xml:space="preserve">{spaces}{esc(title)}</w:t></w:r>\n'
        f'    </w:p>'
    )
    return xml[:para_start - len('<w:p ')] + new_para_xml + xml[para_end:]


def replace_attachments(xml: str, items: list) -> str:
    """Replace everything from เอกสารแนบ paragraph to (not including) sectPr."""
    attach_start = xml.find(f'w14:paraId="{PARA_ATTACH_HDR}"')
    if attach_start == -1:
        return xml
    attach_start = xml.rfind('<w:p ', 0, attach_start)
    sect_start   = xml.find('<w:sectPr')

    if not items:
        # Remove attachment section entirely
        return xml[:attach_start] + xml[sect_start:]

    new_attach = build_attachments(items)
    return xml[:attach_start] + new_attach + xml[sect_start:]


# Thai month names (index 0 = January)
THAI_MONTHS = [
    'มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน',
    'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม',
    'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม',
]

def today_th():
    """Return (day_str, month_th, be_year_str) for today's date."""
    today = date.today()
    be_year = today.year + 543
    return str(today.day), THAI_MONTHS[today.month - 1], str(be_year)


def replace_date(xml: str, day: str, month_th: str, be_year: str) -> str:
    """Replace วันที่ runs: day (' 16'), month (' มิถุนายน'), year ('2566').

    In the template, day and month each have a leading space in their run text.
    The year run is standalone (no leading space).
    """
    # Day: first run matching ' <digits>'
    xml = re.sub(
        r'(<w:t xml:space="preserve"> )\d+(</w:t>)',
        lambda m: f'{m.group(1)}{day}{m.group(2)}',
        xml, count=1
    )
    # Month: run containing Thai month name
    for m_name in THAI_MONTHS:
        xml = xml.replace(
            f'<w:t xml:space="preserve"> {m_name}</w:t>',
            f'<w:t xml:space="preserve"> {month_th}</w:t>',
            1
        )
        if month_th in xml:
            break
    # Year: standalone year run (4 digits) — the template has it split as '256' + '6'
    # Replace both parts using the actual year string split at position -1
    if len(be_year) == 4:
        prefix, last = be_year[:3], be_year[3]
    else:
        prefix, last = be_year[:-1], be_year[-1:]
    # Run containing /256 (doc-number paragraph shares this paragraph — target year standalone)
    # Target: the last pair of digit-split runs in the วันที่ section
    # Pattern: <w:t>PREFIX</w:t> ... <w:t>LAST</w:t>  where these are the year split
    xml = re.sub(
        r'(วฟ[^<]*?/)(\d{3})(<\/w:t>)(.*?)(<w:t>)(\d)(</w:t>)',
        lambda m: (m.group(1) + prefix + m.group(3) +
                   m.group(4) + m.group(5) + last + m.group(7)),
        xml, count=1, flags=re.DOTALL
    )
    # Standalone year run (วันที่ year) — matches '2566' style
    xml = re.sub(r'<w:t>(2\d{3})</w:t>',
                 f'<w:t>{be_year}</w:t>', xml, count=1)
    return xml


def replace_doc_number(xml: str, doc_running: str, be_year: str) -> str:
    """Replace document running number and year in the ที่ field.

    Template pattern across two runs: 'วฟ         /256' + '6'
    Result: 'วฟ         /YYYY_PREFIX' + 'YYYY_LAST'
    """
    if len(be_year) == 4:
        prefix, last = be_year[:3], be_year[3]
    else:
        prefix, last = be_year[:-1], be_year[-1:]
    # Replace the split year in the doc-number runs
    xml = re.sub(
        r'(วฟ\s+/)(\d+)(<\/w:t>)(.*?)(<w:t[^>]*>)(\d)(</w:t>)',
        lambda m: (m.group(1) + doc_running + '/' if doc_running else m.group(1)) +
                  prefix + m.group(3) + m.group(4) + m.group(5) + last + m.group(7),
        xml, count=1, flags=re.DOTALL
    )
    return xml


# ──────────────────────────────────────────────────────────────
# Pipeline
# ──────────────────────────────────────────────────────────────

DOCX_SCRIPTS = '/mnt/skills/public/docx/scripts'


def find_unpack():
    p = os.path.join(DOCX_SCRIPTS, 'office/unpack.py')
    if os.path.exists(p):
        return p
    raise FileNotFoundError('unpack.py not found at ' + p)


def find_pack():
    p = os.path.join(DOCX_SCRIPTS, 'office/pack.py')
    if os.path.exists(p):
        return p
    raise FileNotFoundError('pack.py not found at ' + p)


def generate(config: dict, template_path: str, output_path: str) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        unpacked = os.path.join(tmpdir, 'unpacked')

        # 1. Unpack template
        subprocess.run(
            ['python3', find_unpack(), template_path, unpacked],
            check=True, capture_output=True, text=True
        )

        doc_xml_path = os.path.join(unpacked, 'word', 'document.xml')
        with open(doc_xml_path, 'r', encoding='utf-8') as f:
            xml = f.read()

        # 2. เรื่อง
        subject = config.get('เรื่อง', '')
        if subject:
            xml = replace_subject(xml, subject)

        # 3. Body
        body_xml = build_body(config.get('เนื้อหา', []))
        xml = replace_body(xml, body_xml)

        # 4. Signature title
        sig = config.get('ลงนาม', {})
        if sig.get('ตำแหน่ง'):
            xml = replace_sig_title(xml, sig['ตำแหน่ง'])

        # 5. Attachments
        attachments = config.get('เอกสารแนบ', [])
        xml = replace_attachments(xml, attachments)

        # 6. วันที่ — ใช้วันที่ปัจจุบัน (พ.ศ.) เป็น default
        cfg_date = config.get('วันที่', {})
        if isinstance(cfg_date, str):
            # Legacy: single string treated as day only
            default_day, default_month, default_year = today_th()
            day_val   = cfg_date or default_day
            month_val = config.get('เดือน', default_month)
            year_val  = config.get('ปี', default_year)
        elif isinstance(cfg_date, dict):
            default_day, default_month, default_year = today_th()
            day_val   = cfg_date.get('วัน',   default_day)
            month_val = cfg_date.get('เดือน', default_month)
            year_val  = cfg_date.get('ปี',    default_year)
        else:
            day_val, month_val, year_val = today_th()

        xml = replace_date(xml, day_val, month_val, year_val)

        # 7. เลขที่หนังสือ — ใช้ปี พ.ศ. ปัจจุบันเป็น default
        doc_running = config.get('ที่', '')
        xml = replace_doc_number(xml, doc_running, year_val)

        with open(doc_xml_path, 'w', encoding='utf-8') as f:
            f.write(xml)

        # 8. Repack
        result = subprocess.run(
            ['python3', find_pack(), unpacked, output_path,
             '--original', template_path],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print('Pack stderr:', result.stderr, file=sys.stderr)
            raise RuntimeError(f'pack.py failed:\n{result.stdout}\n{result.stderr}')

        print(f'✓ Memo generated: {output_path}')
        print(result.stdout)


# ──────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate ECE KMUTNB memo (.docx)')
    parser.add_argument('--config',   required=True,  help='Path to JSON config file')
    parser.add_argument('--output',   required=True,  help='Output .docx path')
    parser.add_argument('--template', default=None,   help='Override template path')
    args = parser.parse_args()

    # Resolve template path
    if args.template:
        template = args.template
    else:
        skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template  = os.path.join(skill_dir, 'assets', 'template.docx')

    if not os.path.exists(template):
        print(f'ERROR: Template not found at {template}', file=sys.stderr)
        sys.exit(1)

    with open(args.config, 'r', encoding='utf-8') as f:
        config = json.load(f)

    generate(config, template, args.output)
