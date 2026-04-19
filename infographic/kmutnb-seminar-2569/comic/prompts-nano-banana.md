# Comic Prompts สำหรับ Nano Banana (Gemini 2.5 Flash Image)

คอมมิค 6 ช่อง "Level Up การทำรายงานด้วยคู่หู AI"

**ใช้ได้ที่:** Google AI Studio (ฟรี) → https://aistudio.google.com/ เลือก model `gemini-2.5-flash-image` หรือ Gemini app

## 🎯 จุดเด่นของ Nano Banana ที่จะใช้ประโยชน์
- **Character consistency สูง**: generate panel 1 ให้ดีก่อน แล้ว upload รูปกลับเข้าไปเป็น reference สำหรับ panel 2–6
- **ภาษาธรรมชาติ**: ไม่ต้องใช้ `--ar`, `--niji` ฯลฯ เขียนบรรยายเหมือนคุยกันธรรมดา
- **Multi-image input**: ส่งรูป panel 1 + description ของ panel ถัดไป ได้เลย
- **เขียนข้อความในภาพได้**: สามารถลองให้ใส่ข้อความภาษาอังกฤษหรือไทยในภาพได้ แต่ข้อความไทยยังไม่เสถียร 100% → แนะนำให้บอลลูนว่างไว้ก่อน

---

## 🧑 Character Reference Prompt (Panel 1 — Generate ก่อน)

**Prompt แรกสุด** (ใช้สร้างตัวละครและสไตล์ให้เป็นต้นแบบ):

```
Create a Japanese manga / modern anime style comic panel, square 1:1 composition.

Main character "Ton" — a Thai male university staff member, late 20s to early 30s, short neat black hair with slight side-part, warm brown eyes, light-tan skin, friendly approachable face, simple silver-framed glasses, wearing a navy-blue polo shirt with a small embroidered university logo over a white undershirt, beige chinos, wristwatch on left hand.

Scene for this panel: Ton sits slumped at a cluttered home office desk late at night. Both his hands grip his head in frustration, elbows resting on the desk. He stares at a completely empty, glowing white computer monitor in front of him. Beside him there is a tall precarious stack of thick books and paper folders threatening to topple over. A small desk lamp casts warm yellow pool of light on his workspace, while the rest of the room fades into deep navy-blue shadows. A round wall clock behind him clearly reads 11:15 PM.

Mood: overwhelmed, stressed, late-night despair, the "where do I even start" feeling.

Manga visual language: a big shiny sweat drop on his forehead, vertical stress lines floating above his head, soft dotted screentone shading on the walls to convey heavy atmosphere. Include one empty blank speech bubble near his mouth (no text inside — text will be added later). Clean crisp line art, cel-shading with soft screentones, expressive anime facial expression, warm cinematic color palette.

Do not include any text, letters, captions, or watermarks in the image. Keep all speech bubbles completely empty.
```

> หลัง generate Panel 1 ออกมาดีแล้ว → **Save รูปไว้** แล้ว **upload กลับเข้า chat** ก่อน prompt ของ Panel 2–6 ทุกครั้ง

---

## 🎬 Panel 2 — "เรียกคู่หู Digital"

**Upload Panel 1 image + prompt:**

```
Using the exact same character "Ton" from the reference image I just shared — same face, same hair, same navy-blue polo shirt with white undershirt, same silver-framed glasses, same age — create the NEXT panel in this manga-style comic series. Maintain identical art style, line weight, color palette, and screentone treatment. Square 1:1 composition.

New scene: Ton now sits upright at the same desk, a hopeful energized pose. His fingers rest on the keyboard, he leans slightly forward with his mouth open in a delighted "Oh!" expression, eyes sparkling with amazement. The computer monitor now glows bright — the screen displays a clean AI chat interface with a cute friendly round robot avatar on the left side, and a neat outline of bullet points numbered "1. 2. 3." is appearing in sequence (showing typing cursor effect).

Mood: amazement, hope, the "aha" moment — complete emotional contrast to panel 1.

Manga visual language: sparkle stars around the edges of the monitor, light rays bursting outward from the screen toward Ton's face, his eyes showing the classic anime "sparkle eye" shine. Include two empty blank speech bubbles — one above Ton's head, one near the robot avatar on screen.

Do not include any text, letters, or captions. Keep all speech bubbles completely empty.
```

---

## 🎬 Panel 3 — "นักสืบข้อมูล"

**Upload Panel 1 (หรือ Panel 2 ที่ดีสุด) + prompt:**

```
Using the exact same character "Ton" from the reference image — same face, hair, glasses, navy polo shirt, same art style as the previous panels — create the next panel. Keep consistent manga/anime line work, coloring, and screentones. Square 1:1 composition.

New scene: Close-up medium shot from the side. Ton leans close to his monitor, one hand on the mouse, wearing a focused impressed expression with a small half-smile. The monitor prominently displays a large magnifying glass icon hovering over a stack of English academic research papers filled with graphs, equations, and dense text blocks. On the right side of the screen, a tidy 5-line summary bullet list appears highlighted in soft yellow. A visual metaphor of a thick paper stack shrinking down to a few concise lines is visible.

Mood: focused, efficient, detective-like investigation.

Manga visual language: speed lines radiating outward from the magnifying glass icon, small motion streaks suggesting rapid scanning, soft concentration lines on Ton's forehead. Include one empty blank speech bubble above Ton.

Do not render any text, letters, or captions anywhere in the image. The research papers should show abstract squiggles suggesting text, not real words. All speech bubbles remain empty.
```

---

## 🎬 Panel 4 — "อย่าเชื่อใจ 100%"

**Upload reference image + prompt:**

```
Using the exact same character "Ton" from the reference image — identical appearance, clothing, and art style as the previous panels — create the next comic panel. Maintain the same manga line art, cel-shading, and color palette. Square 1:1 composition.

New scene: Medium shot, Ton facing 3/4 toward the viewer. He has a strongly skeptical suspicious expression — one eyebrow sharply raised, eyes narrowed, lips pressed into a doubting thin line. His right hand holds up a smartphone displaying an official-looking library or news website with a green verified checkmark badge. His left hand points questioningly at the computer monitor, which shows an AI chat output with a bold statistic number highlighted. A bright yellow warning triangle icon with an exclamation mark floats prominently between the phone and the monitor.

Mood: cautious, critical thinking, fact-checking vigilance — "wait a minute, let me verify this."

Manga visual language: several floating question marks around Ton's head, a small sweat drop near his temple, thin vertical hesitation lines coming down from the monitor, a small shocked-halt "pause" symbol. Include one empty blank speech bubble above Ton and one small empty thought bubble near the warning icon.

Do not include any readable text, letters, or captions. Keep all speech bubbles empty.
```

---

## 🎬 Panel 5 — "ขัดเกลาให้สละสลวย"

**Upload reference image + prompt:**

```
Using the exact same character "Ton" from the reference — matching face, hair, glasses, navy polo shirt, and matching the established manga art style from all previous panels — create the next comic panel. Square 1:1 composition.

New scene: Over-the-shoulder shot from behind and slightly above Ton. He types at his keyboard with a calm satisfied half-smile visible in profile. The monitor displays a split-screen "before vs after" text editor view: on the left half, plain casual text with red squiggly underline marks indicating errors; on the right half, the same text elegantly refined into polished formal Thai academic prose (shown as stylized abstract text blocks, not real readable letters), with soft golden shine effects glowing on the refined version. A small friendly round robot AI assistant icon floats in the corner of the screen holding a tiny glowing polish wand.

Mood: satisfied, polished, craftsmanlike refinement — the "making it beautiful" stage.

Manga visual language: sparkle-shine stars on the refined text, small floating light particles drifting around the screen, a soft warm glow around Ton's hands. Include two empty blank speech bubbles — one near Ton, one near the robot icon on screen.

Do not render any actual text or readable letters. The text in the editor should be abstract line patterns suggesting prose, not real words. All speech bubbles remain empty.
```

---

## 🎬 Panel 6 — "ความสำเร็จที่ภาคภูมิใจ"

**Upload reference image + prompt:**

```
Using the exact same character "Ton" from the reference — identical to all previous panels in face, hair, glasses, navy polo shirt, and art style — create the FINAL triumphant panel in this 6-panel manga comic series. Maintain the same line work and coloring. Square 1:1 composition.

New scene: Hero shot, low camera angle looking slightly up at Ton, making him appear heroic. He stands tall and confident in the center of the frame, both hands proudly holding up a beautifully bound thick report with a glossy navy-blue cover and gold-foil embossed decorative title design. He wears a huge confident beaming smile, eyes bright with pride and a hint of joyful moisture. His posture conveys a thumbs-up energy even while holding the report. To his right stands a friendly translucent holographic silhouette of a round cute robot AI companion, softly glowing light blue, also giving an enthusiastic clear thumbs-up gesture.

Mood: triumphant, celebratory, proud human-AI partnership victory.

Manga visual language: classic shonen manga radial speed lines bursting outward behind Ton, sparkling stars and confetti scattered in the foreground, golden light rays streaming from behind him, small "kira-kira" shine effects gleaming on the report cover. Include two empty blank speech bubbles (one above Ton, one above the robot) and one empty horizontal ribbon banner at the bottom of the panel ready to hold a closing tagline.

Do not include any readable text, letters, or captions. Keep all speech bubbles and the banner ribbon completely empty — blank white inside.
```

---

## 💡 Workflow แนะนำใน Google AI Studio

1. เปิด https://aistudio.google.com → เลือก model **`gemini-2.5-flash-image`** (Nano Banana)
2. Paste prompt ของ Panel 1 → Generate หลายรอบจนได้ look ที่ถูกใจ
3. **Save รูป Panel 1** ที่ดีที่สุดไว้
4. สำหรับ Panel 2–6: ในแชทใหม่แต่ละครั้ง
   - Upload รูป Panel 1 เป็น reference (กดไอคอน 📎 attach)
   - Paste prompt ของ panel ถัดไป
   - Generate
5. ถ้าตัวละครเพี้ยน → บอก "the character should match the reference image more closely — same face shape, same glasses"
6. เอาภาพที่ได้ไปไว้ที่ `infographic/kmutnb-seminar-2569/comic/` ตั้งชื่อ `panel_1.png` … `panel_6.png`
7. ใส่ข้อความไทยลงบอลลูนด้วย Canva/Figma/Photopea (ดูตารางบทพูดใน [prompts.md](prompts.md))

## 🔧 Tips เฉพาะ Nano Banana

- **Iterative editing**: ถ้ารูปใกล้จะใช่แล้วแต่มีจุดเล็กๆ ที่ต้องแก้ → บอกเฉพาะจุดนั้น เช่น `"keep everything the same but change the clock to show 11:30 PM"`
- **Multi-reference**: Nano Banana รับได้หลายรูป → upload ทั้ง Panel 1 **และ** Panel ก่อนหน้า เพื่อ lock ทั้ง character + scene style
- **ถ้าข้อความเพี้ยน**: บอก `"remove all text from the image, keep speech bubbles completely blank and empty"` — Nano Banana จะลบให้
- **เพิ่มข้อความไทยในภาพ**: ลองบอกได้ เช่น `"add Thai text in the speech bubble saying: หัวข้อรายงานกว้างเป็นมหาสมุทรเลย"` แต่ยังไม่เสถียร — fallback คือแก้ใน Canva

## 📚 ดูบทพูดภาษาไทยของแต่ละช่อง

ดูตาราง Thai Dialogue ในไฟล์ [prompts.md](prompts.md) ช่วงท้าย
