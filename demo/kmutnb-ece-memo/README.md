# AI-workshop — KMUTNB ECE Department

โครงการ AI tools สำหรับงานวิชาการ ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์
คณะวิศวกรรมศาสตร์ มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ

---

## โครงสร้างโฟลเดอร์

```
AI-workshop/
├── README.md
├── skills/
│   ├── kmutnb-ece-memo.skill          ← ติดตั้งใน Claude ผ่าน Settings → Skills
│   └── kmutnb-ece-memo/               ← source code ของ skill
│       ├── SKILL.md                   ← คำสั่งหลัก + trigger keywords
│       ├── assets/
│       │   └── template.docx          ← template บันทึกข้อความ ECE KMUTNB
│       ├── scripts/
│       │   └── generate_memo.py       ← script สร้าง docx จาก JSON config
│       └── references/
│           └── template_structure.md  ← แผนที่ XML ของ template
└── examples/
    ├── configs/                       ← ตัวอย่าง JSON config แต่ละประเภท
    │   ├── ขออนุมัติจัดโครงการ.json
    │   ├── ขออนุมัติจัดซื้อ.json
    │   └── ขออนุมัติเดินทาง.json
    └── outputs/                       ← ตัวอย่างผลลัพธ์ .docx ที่สร้างแล้ว
        ├── ขออนุมัติจัดโครงการ_AI_Seminar.docx
        └── ขออนุมัติจัดซื้อ_IoT.docx
```

---

## Skills ที่มี

### `kmutnb-ece-memo`
สร้างบันทึกข้อความราชการภายใน ECE KMUTNB เป็นไฟล์ .docx
พร้อมโลโก้ มจพ. เส้นประตกแต่ง และ TH Sarabun New font ครบถ้วน

**ติดตั้ง:** Settings → Skills → Install from file → `skills/kmutnb-ece-memo.skill`

**ใช้งาน:** พิมพ์ใน Claude ว่า
- "ร่างบันทึกข้อความขออนุมัติ..."
- "สร้าง memo ภาควิชาเรื่อง..."
- "บันทึกข้อความขออนุมัติจัดซื้อ..."

**รัน script ตรงๆ:**
```bash
python3 skills/kmutnb-ece-memo/scripts/generate_memo.py \
  --config examples/configs/ขออนุมัติจัดโครงการ.json \
  --template skills/kmutnb-ece-memo/assets/template.docx \
  --output output.docx
```

**Config JSON — ค่า default อัตโนมัติ:**
- `วันที่` → วันนี้ (แปลง CE → พ.ศ. อัตโนมัติ)
- `ที่` → `วฟ /YYYY` โดย YYYY = พ.ศ. ปัจจุบัน

---

## Dependencies

- Python 3.x
- docx skill scripts จาก Claude (`/mnt/skills/public/docx/scripts/`)
  - `office/unpack.py`
  - `office/pack.py`
