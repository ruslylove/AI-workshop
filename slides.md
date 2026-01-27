---
# Theme & Config
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## AI for Engineering Support
  KMUTNB Workshop (Tailored based on Survey)
drawings:
  persist: false
transition: slide-left
title: AI for Engineering Support

# Fonts
fonts:
  sans: 'Kanit'
  serif: 'Sarabun'
  mono: 'Fira Code'
---

# 🤖 AI for Smart Support
## ยกระดับงานสายสนับสนุนด้วยปัญญาประดิษฐ์
(Customized for KMUTNB Engineering Team)

<div class="pt-8">
  <div class="bg-white/10 backdrop-blur-md p-4 rounded-xl inline-block border border-white/20">
    <p class="text-lg font-bold text-white mb-2">Agenda (ฉบับตามใจผู้เรียน)</p>
    <div class="text-left text-sm text-gray-200 grid grid-cols-2 gap-8">
      <div>
        <b class="text-blue-300">Part 1: บรรยาย & สาธิต (90 นาที)</b><br>
        - <b>Survey Results:</b> เสียงจากพวกเราเอง<br>
        - <b>Demo:</b> แก้ปัญหา Top 3 (เอกสาร/แปล/Excel)<br>
        - <b>Showcase:</b> งานอาคารฯ & งานพัสดุ
      </div>
      <div>
        <b class="text-orange-300">Part 2: ปฏิบัติ (90 นาที)</b><br>
        - <b>Workshop:</b> Super Support Challenge<br>
        - <b>Tools:</b> แจก Web App สำเร็จรูป<br>
        - <b>Competition:</b> ประชันไอเดีย (ไม่เครียด!)
      </div>
    </div>
  </div>
</div>

---
layout: center
---

# 📣 เสียงจากแบบสอบถาม (Survey Insights)
"เรารู้ว่าคุณเจอปัญหาอะไร... วันนี้เราจะมาแก้สิ่งนั้น!"

<div class="grid grid-cols-2 gap-8 mt-6 text-left">
  <div class="bg-blue-50 p-5 rounded-xl border-l-4 border-blue-500">
    <h3 class="text-xl font-bold text-blue-700 mb-2">🏆 Top 3 ปัญหาที่อยากแก้</h3>
    <ul class="list-disc pl-5 space-y-2 text-gray-700">
      <li><b>อันดับ 1:</b> ร่างหนังสือราชการ & อีเมล (ร่วมกับ แปลภาษา)</li>
      <li><b>อันดับ 1 (ร่วม):</b> จัดการสูตร Excel & ข้อมูลเยอะๆ</li>
      <li><b>อันดับ 2:</b> งานแจ้งซ่อม / ประกาศปิดพื้นที่ (งานอาคารฯ)</li>
    </ul>
  </div>

  <div class="bg-green-50 p-5 rounded-xl border-l-4 border-green-500">
    <h3 class="text-xl font-bold text-green-700 mb-2">🥰 ความคาดหวังในวันนี้</h3>
    <div class="italic text-gray-600 bg-white p-3 rounded shadow-sm">
      "ไม่เคร่งเครียด", "ไม่มีความกดดัน", <br>"นำไปใช้งานได้จริง", "ช่วยงานซ้ำซากได้"
    </div>
    <div class="mt-4 text-sm font-bold text-green-800">
      ✅ สัญญาครับ! วันนี้เน้นสนุก ใช้งานจริง ไม่วิชาการจ๋า
    </div>
  </div>
</div>

---
layout: section
---

# Part 1: Unlock AI Potential
รู้จักเครื่องมือที่จะมาช่วยเรา "หายเหนื่อย"

---

# 🧠 Generative AI คืออะไร? (ฉบับรวบรัด)
มันคือ "ลูกน้องคนใหม่" ที่...

<div class="grid grid-cols-3 gap-6 mt-8 text-center">
  <div v-click class="p-4 bg-white rounded-xl shadow-lg transform hover:scale-105 transition">
    <div class="text-5xl mb-3">📚</div>
    <h3 class="font-bold text-gray-700">อ่านเก่ง</h3>
    <p class="text-xs text-gray-500 mt-2">อ่านระเบียบ 20 หน้า<br>สรุปเหลือ 5 บรรทัดได้</p>
  </div>
  <div v-click class="p-4 bg-white rounded-xl shadow-lg transform hover:scale-105 transition">
    <div class="text-5xl mb-3">✍️</div>
    <h3 class="font-bold text-gray-700">เขียนเก่ง</h3>
    <p class="text-xs text-gray-500 mt-2">ร่างหนังสือทางการ<br>แปลอังกฤษเป๊ะเวอร์</p>
  </div>
  <div v-click class="p-4 bg-white rounded-xl shadow-lg transform hover:scale-105 transition">
    <div class="text-5xl mb-3">💡</div>
    <h3 class="font-bold text-gray-700">คิดเก่ง</h3>
    <p class="text-xs text-gray-500 mt-2">ช่วยคิดแคปชัน<br>ช่วยวิเคราะห์ข้อมูล</p>
  </div>
</div>

<div class="mt-8 text-sm text-gray-500">
  (ส่วนใหญ่ในห้อง "เคยลองเล่นบ้าง" แล้ว... วันนี้เราจะมาทำให้ "เซียน" ครับ!)
</div>

---

# 🥊 เปรียบเทียบ 3 เทพ (ฉบับเลือกใช้ง่าย)

<div class="grid grid-cols-3 gap-4 mt-4 text-sm">

<div class="border rounded-xl p-4 bg-white shadow-sm">
  <div class="flex items-center gap-2 mb-2">
    <carbon-bot class="text-2xl text-green-600" />
    <b class="text-green-700">ChatGPT</b>
  </div>
  <ul class="list-disc pl-4 space-y-1 text-xs text-gray-600">
    <li><b>เก่งสุด:</b> ภาษาไทยลื่นไหล, ความคิดสร้างสรรค์</li>
    <li><b>เหมาะกับ:</b> ร่างหนังสือ, แปลภาษา, คิดงาน PR</li>
    <li><b>Tip:</b> รุ่นฟรีเก่งมากแล้ว รุ่น Plus ยิ่งเทพ</li>
  </ul>
</div>

<div class="border rounded-xl p-4 bg-blue-50 shadow-sm border-blue-200">
  <div class="flex items-center gap-2 mb-2">
    <carbon-star class="text-2xl text-blue-600" />
    <b class="text-blue-700">Gemini (Google)</b>
  </div>
  <ul class="list-disc pl-4 space-y-1 text-xs text-gray-600">
    <li><b>เก่งสุด:</b> ค้นข้อมูลปัจจุบัน, เชื่อม Docs/Sheet</li>
    <li><b>เหมาะกับ:</b> งานวิจัย, สรุปข่าว, งานสารบรรณ</li>
    <li><b>Tip:</b> ส่งออกเข้า Google Docs ได้เลย!</li>
  </ul>
</div>

<div class="border rounded-xl p-4 bg-white shadow-sm">
  <div class="flex items-center gap-2 mb-2">
    <carbon-ibm-watson-knowledge-studio class="text-2xl text-orange-600" />
    <b class="text-orange-700">Claude</b>
  </div>
  <ul class="list-disc pl-4 space-y-1 text-xs text-gray-600">
    <li><b>เก่งสุด:</b> อ่านเอกสารยาวๆ แม่นยำ, เขียนโค้ด</li>
    <li><b>เหมาะกับ:</b> สรุป TOR, ตรวจร่างสัญญา</li>
    <li><b>Tip:</b> ภาษาไทยอาจจะดูทางการนิดนึง</li>
  </ul>
</div>

</div>

---
layout: center
---

# 🗝️ สูตรลับสั่งงาน (Prompt Engineering)
สั่งยังไงให้ได้ดั่งใจ? (C-T-F Formula)

<div class="mt-6 p-6 bg-gray-50 rounded-xl border-l-8 border-indigo-500 text-left shadow-lg">
  <div class="grid grid-cols-1 gap-4 text-lg">
    <div>1. 🎭 <b>Role (บทบาท):</b> "รับบทเป็น <b>เจ้าหน้าที่งานอาคารฯ</b>..."</div>
    <div>2. 📝 <b>Task (งาน):</b> "ช่วยร่าง <b>ประกาศแจ้งปิดซ่อมลิฟต์</b>..."</div>
    <div>3.  Context (บริบท): "ปิด 2 วัน ให้ใช้บันไดหนีไฟแทน..."</div>
    <div>4. 📦 <b>Format (รูปแบบ):</b> "ขอภาษา <b>สุภาพแต่ชัดเจน</b>..."</div>
  </div>
</div>

---
layout: section
---

# 🎬 ช่วงสาธิต: Live Demos (30 นาที)
แก้โจทย์จริงจากแบบสอบถาม!

---

# 🔮 Demo 1: งานสารบรรณ & วิเทศฯ (Top Vote!)
**Scenario:** ร่างหนังสือ + แปลอีเมลถึง Professor ญี่ปุ่น

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <h3 class="font-bold text-blue-600">โจทย์จากทางบ้าน:</h3>
    <ul class="list-disc pl-5 text-sm space-y-2">
      <li>ร่างบันทึกข้อความแบบทางการ (ไม่ต้องคิดคำเอง)</li>
      <li>แปลอีเมลเชิญวิทยากรต่างชาติ (ขอภาษา Business English)</li>
    </ul>
    <div class="mt-4 bg-gray-100 p-2 rounded text-xs">
      <b>Action:</b> ใช้ ChatGPT ร่างภาษาไทย -> แล้วสั่ง "Translate to formal English" ต่อทันที
    </div>
  </div>
  <div class="flex items-center justify-center bg-blue-50 rounded-xl">
    <span class="text-6xl">🌍</span>
  </div>
</div>

---

# 🔮 Demo 2: งานอาคารสถานที่ & ยานพาหนะ (VIP Group)
**Scenario:** ประกาศปิดพื้นที่ & แจ้งซ่อม

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <h3 class="font-bold text-yellow-600">โจทย์จากทางบ้าน:</h3>
    <ul class="list-disc pl-5 text-sm space-y-2">
      <li>ร่างประกาศปิดปรับปรุงห้องน้ำ อาคาร 81 (ด่วน!)</li>
      <li>ต้องแจ้งนิสิตและบุคลากรไม่ให้หงุดหงิด</li>
    </ul>
    <div class="mt-4 bg-gray-100 p-2 rounded text-xs">
      <b>Prompt Idea:</b> "ร่างประกาศปิดปรับปรุงห้องน้ำ... ขอสไตล์ 'ขออภัยในความไม่สะดวก' และแนะนำห้องน้ำใกล้เคียง พร้อมอีโมจิ 🙏"
    </div>
  </div>
  <div class="flex items-center justify-center bg-yellow-50 rounded-xl">
    <span class="text-6xl">🚧</span>
  </div>
</div>

---

# 🔮 Demo 3: งานคลัง & แผน (Excel & Data)
**Scenario:** สรุปราคาวัสดุ & วิเคราะห์ข้อมูล

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <h3 class="font-bold text-green-600">โจทย์จากทางบ้าน:</h3>
    <ul class="list-disc pl-5 text-sm space-y-2">
      <li>มีรายการวัสดุและราคาใน Excel เยอะมาก</li>
      <li>อยากรู้ว่า "รายการไหนราคาขึ้น?" และ "สรุปยอดรวมแต่ละหมวด"</li>
    </ul>
    <div class="mt-4 bg-gray-100 p-2 rounded text-xs">
      <b>Action:</b> โยนไฟล์ Excel ใส่ ChatGPT (Data Analyst) -> สั่ง "สร้างตารางเปรียบเทียบราคา และทำกราฟสรุปยอด"
    </div>
  </div>
  <div class="flex items-center justify-center bg-green-50 rounded-xl">
    <span class="text-6xl">📉</span>
  </div>
</div>

---

# 🔮 Demo 4: ศูนย์คอมฯ & PR (Special Request)
**Scenario:** ทำ Infographic จากกำหนดการ

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <h3 class="font-bold text-purple-600">โจทย์พิเศษ:</h3>
    <ul class="list-disc pl-5 text-sm space-y-2">
      <li>"นำกำหนดการสัมมนา ให้ AI สร้างเป็น Infographic"</li>
    </ul>
    <div class="mt-4 bg-gray-100 p-2 rounded text-xs">
      <b>Tools แนะนำ:</b> <br>
      1. <b>Canva Magic Design:</b> โยน Text -> ได้ภาพ<br>
      2. <b>Piktochart AI:</b> เน้นทำ Info โดยเฉพาะ<br>
      (สาธิต Canva เพราะทุกคนน่าจะคุ้นเคยสุด)
    </div>
  </div>
  <div class="flex items-center justify-center bg-purple-50 rounded-xl">
    <span class="text-6xl">🎨</span>
  </div>
</div>

---
layout: center
class: text-center
---

# 🛠️ เครื่องมือช่วยชีวิต: Engineering AI Prompter
(แจกฟรี! Web App ที่ทำมาเพื่อพวกเราโดยเฉพาะ)

<div class="mt-8 flex justify-center">
  <div class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-6 rounded-2xl shadow-xl max-w-2xl">
    <h2 class="text-2xl font-bold mb-4">Web App รวมสูตรสำเร็จ</h2>
    <p class="mb-4 text-blue-100">รวม 16 สถานการณ์ (ธุรการ, พัสดุ, อาคาร, คอมฯ ครบ!)<br>แค่เลือก -> เติมคำ -> กด Copy -> ใช้ได้เลย!</p>
    <div class="text-xs bg-white/20 p-2 rounded">
      (เราจะมาลองเล่นตัวนี้กันเต็มๆ ในช่วงบ่ายครับ)
    </div>
  </div>
</div>

---
layout: cover
background: https://source.unsplash.com/random/1920x1080/?coffee,break
---

# พักรับประทานอาหารกลางวัน
(12.00 - 13.00 น.)
พักผ่อนให้เต็มที่ ช่วงบ่ายมาร่วมสนุกกันครับ!

---
layout: section
---

# Part 2: Workshop
(13.00 - 14.30 น.)
"Super Support Challenge" (แข่งกันสนุกๆ)

---

# 🎮 กติกาการแข่งขัน (Challenge Rules)

<div class="grid grid-cols-2 gap-8 mt-6">
  
  <div class="bg-white p-5 rounded-xl shadow border-l-4 border-blue-500 text-left">
    <h3 class="text-xl font-bold text-blue-700 mb-4">ขั้นตอน</h3>
    <ol class="list-decimal pl-5 space-y-3">
      <li>จับคู่ หรือทำงานเป็นกลุ่มตามโต๊ะ</li>
      <li>เลือก <b>1 โจทย์ปัญหา</b> จาก Web App (หรือปัญหาจริงที่เจอ)</li>
      <li>ระดมสมองเขียน <b>Prompt</b> สั่ง AI</li>
      <li>ส่งผลงาน (Prompt + Output) เข้ากลุ่ม Line</li>
    </ol>
  </div>

  <div class="bg-white p-5 rounded-xl shadow border-l-4 border-orange-500 text-left">
    <h3 class="text-xl font-bold text-orange-700 mb-4">เกณฑ์การตัดสิน</h3>
    <div class="text-sm text-gray-600 mb-2">ตัดสินโดย <b>AI Judge (กรรมการ AI)</b> + วิทยากร</div>
    <ul class="list-disc pl-5 space-y-2">
      <li>🎯 <b>Practicality:</b> เอาไปใช้ได้จริงไหม?</li>
      <li>🗣️ <b>Prompt Quality:</b> สั่งงานละเอียดแค่ไหน?</li>
      <li>💡 <b>Creativity:</b> ไอเดียสร้างสรรค์?</li>
    </ul>
  </div>

</div>

---

# 🏆 ตัวอย่างโจทย์ (Challenge Missions)

<div class="grid grid-cols-3 gap-4 mt-4 text-xs">
  <div class="bg-blue-50 p-3 rounded border border-blue-200">
    <b class="text-blue-700 block mb-1">1. ทีมธุรการ/วิเทศฯ</b>
    ร่างอีเมลตอบรับ Professor ญี่ปุ่น + แจ้งตารางทัวร์คณะ
  </div>
  <div class="bg-yellow-50 p-3 rounded border border-yellow-200">
    <b class="text-yellow-700 block mb-1">2. ทีมอาคาร/ยานพาหนะ</b>
    ร่างประกาศ "งดจอดรถหน้าตึก" เพื่อตีเส้นจราจรใหม่
  </div>
  <div class="bg-green-50 p-3 rounded border border-green-200">
    <b class="text-green-700 block mb-1">3. ทีมคลัง/พัสดุ</b>
    เปรียบเทียบสเปกคอมฯ 2 รุ่น สรุปให้กรรมการตรวจรับ
  </div>
  <div class="bg-purple-50 p-3 rounded border border-purple-200">
    <b class="text-purple-700 block mb-1">4. ศูนย์คอม/บริการการศึกษา</b>
    ร่าง Q&A ตอบนิสิตเรื่อง "ลืมรหัสผ่าน WiFi / เข้าระบบไม่ได้"
  </div>
  <div class="bg-orange-50 p-3 rounded border border-orange-200">
    <b class="text-orange-700 block mb-1">5. ทีม PR</b>
    คิด Caption เปิดตัว "มาสคอตคณะ" ตัวใหม่ ให้น่ารักน่ากอด
  </div>
  <div class="bg-teal-50 p-3 rounded border border-teal-200">
    <b class="text-teal-700 block mb-1">6. ทีมแผน/วิจัย</b>
    สรุปยอดโครงการย้อนหลัง 3 ปี ทำเป็นตารางเสนอคณบดี
  </div>
</div>

<div class="mt-6 text-center animate-bounce font-bold text-red-600">
  (ไม่มีผิด ไม่มีถูก! ลองเล่นให้เต็มที่!)
</div>

---
layout: center
class: text-center
---

# 🎤 Presentation & AI Judging
โชว์ผลงานขึ้นจอ ให้ AI วิจารณ์สด! (ฮาได้ เต็มที่ได้)

---
layout: end
---

# ขอบคุณครับ
## Q & A

<div class="flex justify-center gap-4 mt-6">
  <a href="#" class="px-4 py-2 bg-blue-600 text-white rounded-lg">Download Slides</a>
  <a href="#" class="px-4 py-2 bg-gray-600 text-white rounded-lg">เข้าใช้ Web App</a>
</div>