---
# Theme & Config
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Generative AI มาประยุกต์ใช้ในการทำงาน
  วันที่ 28 มกราคม 2569
  โดย ผศ.ดร.รุสลี่ สุทธวีร์กูล
drawings:
  persist: false
transition: slide-left
title: Generative AI for Work
# Fonts
fonts:
  sans: "Kanit"
  serif: "Sarabun"
  mono: "Fira Code"
---

# 🤖 Generative AI มาประยุกต์ใช้ในการทำงาน
## โครงการสัมมนาบุคลากรสายสนับสนุนวิชาการฯ (28 ม.ค. 69)
<div class="mt-4 text-sm text-gray-600">
  โดย ผศ.ดร.รุสลี่ สุทธวีร์กูล <br>
  ผู้ช่วยคณบดีฝ่ายสารสนเทศ คณะวิศวกรรมศาสตร์
</div>

<div class="absolute bottom-12 left-10">
  <img src="/logo_eng.jpg" class="w-24 h-24 rounded-full shadow-lg border-2 border-white" alt="KMUTNB Engineering Logo">
</div>

<div class="absolute bottom-10 right-10">
  <img src="/qrcode_slides.png" class="w-24 h-24 border-2 border-white rounded-lg shadow-lg" alt="Slides QR Code">
  <div class="text-[8px] text-gray-400 mt-1 text-center">Scan for Slides</div>
</div>


<div class="pt-8">
  <div class="bg-white/10 backdrop-blur-md p-4 rounded-xl inline-block border border-white/20">
    <p class="text-lg font-bold text-white mb-2">Agenda (ฉบับตามใจผู้เรียน)</p>
    <div class="text-left text-sm text-gray-200 grid grid-cols-2 gap-8">
      <div>
        <b class="text-blue-300"># Part 1: บรรยาย & สาธิต
(13.00 - 14.30 น.)</b><br>
        - <b>Survey Results:</b> เสียงจากพวกเราเอง<br>
        - <b>Demo:</b> แก้ปัญหา Top 3 (เอกสาร/แปล/Excel)<br>
        - <b>Showcase:</b> งานอาคารฯ & งานพัสดุ
      </div>
      <div>
        <b class="text-orange-300"># Part 2: ปฏิบัติ
(14.45 - 16.15 น.)</b><br>
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

# รู้จัก AI ใกล้ตัว... (Activities) 🎨
มาลองเล่น AI ง่ายๆ ที่ Google สร้างขึ้น

<div class="flex justify-center mt-8">
  <div class="text-center p-8 border-2 border-dashed border-gray-300 rounded-xl hover:border-blue-500 hover:bg-blue-50 transition cursor-pointer">
    <a href="https://quickdraw.withgoogle.com/" target="_blank">
      <div class="text-6xl mb-4">🖍️</div>
      <h2 class="text-2xl font-bold text-blue-600">Google Quick, Draw!</h2>
      <p class="text-gray-500 mt-2">AI ทายภาพวาดของเรา (ภายใน 20 วินาที)</p>
    </a>
  </div>
</div>

---

# AI vs Gen-AI คืออะไร?
ความแตกต่างที่ต้องรู้

<div class="grid grid-cols-2 gap-8 mt-6">
  <div class="bg-gray-50 p-6 rounded-xl border border-gray-200">
    <h3 class="font-bold text-gray-700 mb-2">🤖 AI (Artificial Intelligence)</h3>
    <p class="text-sm">"ความฉลาดเทียมที่สร้างขึ้นให้กับสิ่งที่ไม่มีชีวิต"</p>
    <ul class="list-disc pl-5 mt-4 text-xs text-gray-600 space-y-2">
      <li>เน้นการวิเคราะห์, จำแนก, หรือทำตามกฎ</li>
      <li>Ex. ระบบสแกนหน้า, ระบบแนะนำ Netflix</li>
    </ul>
  </div>
  <div class="bg-indigo-50 p-6 rounded-xl border border-indigo-200">
    <h3 class="font-bold text-indigo-700 mb-2">✨ Gen-AI (Generative AI)</h3>
    <p class="text-sm">"AI ที่ **สร้าง** ข้อความ, รูปภาพ, หรือสื่ออื่นๆ ได้เอง"</p>
    <ul class="list-disc pl-5 mt-4 text-xs text-gray-600 space-y-2">
      <li>เน้นการ "สร้างใหม่" (Generate)</li>
      <li>Ex. ChatGPT เขียนอีเมล, Midjourney วาดรูป</li>
    </ul>
  </div>
</div>

---

# เปรียบเทียบ 3 เทพ (วัดพลังภาษาไทย) 🇹🇭
ข้อมูลจากการทดสอบจริง (Claude 3.5 Sonnet / ChatGPT 4o / Gemini Advanced)

<div class="grid grid-cols-3 gap-2 mt-4 text-xs">

  <!-- Claude -->
  <div class="border-2 border-orange-200 rounded-xl p-3 bg-orange-50 relative overflow-hidden">
    <div class="absolute top-0 right-0 bg-orange-500 text-white text-[10px] px-2 py-1 rounded-bl">Best Thai</div>
    <div class="flex items-center gap-2 mb-2">
      <b class="text-orange-700 text-lg">Claude 3.5</b>
    </div>
    <div class="space-y-2">
      <div>
        <span class="block text-gray-500">ความเข้าใจภาษาไทย</span>
        <div class="w-full bg-gray-200 rounded-full h-2.5">
          <div class="bg-orange-500 h-2.5 rounded-full" style="width: 98%"></div>
        </div>
        <div class="text-right font-bold text-orange-600">98%</div>
      </div>
      <div>
        <span class="block text-gray-500">การโต้ตอบ</span>
        <div class="text-right font-bold text-orange-600">92%</div>
      </div>
      <p class="mt-2 text-[10px] text-gray-600"><b>จุดเด่น:</b> ภาษาธรรมชาติที่สุด, อ่านไฟล์รูปได้</p>
    </div>
  </div>

  <!-- ChatGPT -->
  <div class="border rounded-xl p-3 bg-white shadow-sm">
    <div class="flex items-center gap-2 mb-2">
      <b class="text-green-700 text-lg">ChatGPT 4o</b>
    </div>
    <div class="space-y-2">
      <div>
        <span class="block text-gray-500">ความเข้าใจภาษาไทย</span>
        <div class="w-full bg-gray-200 rounded-full h-2.5">
          <div class="bg-green-500 h-2.5 rounded-full" style="width: 98%"></div>
        </div>
        <div class="text-right font-bold text-green-600">98%</div>
      </div>
      <div>
        <span class="block text-gray-500">การโต้ตอบ</span>
        <div class="text-right font-bold text-green-600">89%</div>
      </div>
      <p class="mt-2 text-[10px] text-gray-600"><b>จุดเด่น:</b> เก่งรอบด้าน, ฟีเจอร์เยอะ</p>
    </div>
  </div>

  <!-- Gemini -->
  <div class="border rounded-xl p-3 bg-white shadow-sm">
    <div class="flex items-center gap-2 mb-2">
      <b class="text-blue-700 text-lg">Gemini Adv.</b>
    </div>
    <div class="space-y-2">
      <div>
        <span class="block text-gray-500">ความเข้าใจภาษาไทย</span>
        <div class="w-full bg-gray-200 rounded-full h-2.5">
          <div class="bg-blue-500 h-2.5 rounded-full" style="width: 89%"></div>
        </div>
        <div class="text-right font-bold text-blue-600">89%</div>
      </div>
      <div>
        <span class="block text-gray-500">การโต้ตอบ</span>
        <div class="text-right font-bold text-blue-600">85%</div>
      </div>
       <p class="mt-2 text-[10px] text-gray-600"><b>จุดเด่น:</b> เชื่อมต่อ Google Workspace, ฟรีเยอะ</p>
    </div>
  </div>

</div>

<div class="mt-4 text-center text-[10px] text-gray-400">
  *ข้อมูลอ้างอิงจากตารางเปรียบเทียบความสามารถ Gen AI (Anthropic/OpenAI/Google)
</div>

---

# 🥊 เจาะลึก 3 ค่ายใหญ่: จุดเด่น & ราคา (2025)
เลือกให้ถูกโฉลก... งานจะสบายขึ้น 300%

<div class="grid grid-cols-3 gap-4 mt-6">

  <!-- OpenAI -->
  <div class="bg-green-50 p-3 rounded-xl border border-green-200">
    <div class="flex items-center gap-2 mb-2">
      <div class="text-2xl">🟢</div>
      <b class="text-green-700">OpenAI (ChatGPT)</b>
    </div>
    <div class="text-[10px] space-y-2">
      <p><b>รุ่น:</b> GPT-4o / o1</p>
      <div class="bg-white p-2 rounded">
        <b>✅ ข้อดี (Pros):</b>
        <ul class="list-disc pl-3 mt-1 text-gray-600">
          <li><b>All-in-One:</b> เก่งรอบด้าน (เขียน/วาด/Excel)</li>
          <li><b>Voice Mode:</b> คุยเสียงธรรรมชาติสุด</li>
          <li><b>Custom GPTs:</b> มีบอทช่วยงานเยอะ</li>
        </ul>
      </div>
       <div class="bg-green-100 p-2 rounded text-green-800">
        <b>💰 Pack: Plus (~700บ.)</b><br>
        ใช้รุ่น Top ไม่จำกัด*, สร้างรูป DALL-E, วิเคราะห์ Data
      </div>
    </div>
  </div>

  <!-- Anthropic -->
  <div class="bg-orange-50 p-3 rounded-xl border border-orange-200">
    <div class="flex items-center gap-2 mb-2">
      <div class="text-2xl">🟠</div>
      <b class="text-orange-700">Anthropic (Claude)</b>
    </div>
    <div class="text-[10px] space-y-2">
      <p><b>รุ่น:</b> Claude 3.5 Sonnet</p>
      <div class="bg-white p-2 rounded">
        <b>✅ ข้อดี (Pros):</b>
        <ul class="list-disc pl-3 mt-1 text-gray-600">
          <li><b>ภาษาไทย:</b> สละสลวย เป็นธรรมชาติสุด</li>
          <li><b>Coding/Logic:</b> ฉลาดและแม่นยำที่สุด</li>
          <li><b>Artifacts:</b> แยกหน้าต่างดู Code/Doc ได้</li>
        </ul>
      </div>
       <div class="bg-orange-100 p-2 rounded text-orange-800">
        <b>💰 Pack: Pro (~700บ.)</b><br>
        โควต้าคุยเยอะขึ้น 5 เท่า, สร้าง Projects (คลังความรู้)
      </div>
    </div>
  </div>

  <!-- Google -->
  <div class="bg-blue-50 p-3 rounded-xl border border-blue-200">
    <div class="flex items-center gap-2 mb-2">
      <div class="text-2xl">🔵</div>
      <b class="text-blue-700">Google (Gemini)</b>
    </div>
    <div class="text-[10px] space-y-2">
      <p><b>รุ่น:</b> Gemini 1.5 Pro</p>
      <div class="bg-white p-2 rounded">
        <b>✅ ข้อดี (Pros):</b>
        <ul class="list-disc pl-3 mt-1 text-gray-600">
          <li><b>Context:</b> อ่านไฟล์ PDF พันหน้าได้สบาย</li>
          <li><b>Ecosystem:</b> เชื่อม Docs/Drive/Gmail</li>
          <li><b>Free:</b> รุ่นฟรี (Flash) ทำงานเร็วมาก</li>
        </ul>
      </div>
       <div class="bg-blue-100 p-2 rounded text-blue-800">
        <b>💰 Pack: Adv. (~750บ.)</b><br>
        ใช้ 1.5 Pro + <b>แถม Google One 2TB</b>
      </div>
    </div>
  </div>

</div>

<div class="mt-4 text-center text-xs text-gray-500">
  <b>💡 คำแนะนำ:</b> สายวิชาการ/เขียนโค้ด -> <b>Claude</b> | สายทั่วไป/รูปภาพ -> <b>ChatGPT</b> | สายเอกสารเยอะ/Drive -> <b>Gemini</b>
</div>

---

# 🌟 3 เรื่องราว "ชีวิตเปลี่ยน" เพราะ AI (Success Stories)
ทำไมใช้แล้วชีวิตดี๊ดี? (เจ้านายรัก / ลูกน้องเลิฟ / Career พุ่ง)

<div class="grid grid-cols-3 gap-6 mt-8">

  <!-- Case 1: เจ้านายรัก -->
  <div class="bg-white p-5 rounded-xl shadow-lg border-t-4 border-blue-500 relative transform hover:-translate-y-2 transition duration-300">
    <div class="absolute -top-6 left-1/2 transform -translate-x-1/2 bg-blue-500 text-white w-12 h-12 rounded-full flex items-center justify-center text-2xl shadow-md">
      👩‍💼
    </div>
    <div class="mt-6 text-center">
      <h3 class="font-bold text-blue-800 text-lg">พี่สมศรี (งานธุรการ)</h3>
      <p class="text-xs text-gray-400">"เจ้านายรัก เพราะข้อมูลไว"</p>
    </div>
    <div class="mt-4 text-xs text-gray-600 space-y-2 text-left">
      <p>❌ <b>ก่อนหน้า:</b> จดประชุมไม่ทัน สรุปรายงานช้า เจ้านายรอนานจนหงุดหงิด</p>
      <p>✅ <b>ใช้ AI:</b> อัดเสียง -> ถอดความ -> ให้ AI สรุปประเด็นสำคัญใน 1 นาที</p>
      <div class="bg-blue-50 p-2 rounded text-blue-700 font-bold text-center mt-2">
        "เจ้านายปลื้ม! ได้ Data ตัดสินใจทันที ไม่ต้องรอกลับไปพิมพ์"
      </div>
    </div>
  </div>

  <!-- Case 2: ลูกน้อง/นศ. รัก -->
  <div class="bg-white p-5 rounded-xl shadow-lg border-t-4 border-pink-500 relative transform hover:-translate-y-2 transition duration-300">
    <div class="absolute -top-6 left-1/2 transform -translate-x-1/2 bg-pink-500 text-white w-12 h-12 rounded-full flex items-center justify-center text-2xl shadow-md">
      👨‍🏫
    </div>
    <div class="mt-6 text-center">
      <h3 class="font-bold text-pink-800 text-lg">อ.สมชาย (อาจารย์)</h3>
      <p class="text-xs text-gray-400">"นศ. รัก เพราะใส่ใจ"</p>
    </div>
    <div class="mt-4 text-xs text-gray-600 space-y-2 text-left">
      <p>❌ <b>ก่อนหน้า:</b> ตอบไลน์ นศ. เรื่องเดิมๆ จนดึก หน้าตึง กลายเป็นคนดุ</p>
      <p>✅ <b>ใช้ AI:</b> สร้าง Prompt ช่วยตอบคำถาม/ตรวจงานเบื้องต้น เอาเวลาไปให้คำปรึกษาเชิงลึก</p>
      <div class="bg-pink-50 p-2 rounded text-pink-700 font-bold text-center mt-2">
        "มีเวลาคุยกับเด็กมากขึ้น ไม่ต้องหัวหมุนกับงานรูทีน"
      </div>
    </div>
  </div>

  <!-- Case 3: การงานก้าวหน้า -->
  <div class="bg-white p-5 rounded-xl shadow-lg border-t-4 border-purple-500 relative transform hover:-translate-y-2 transition duration-300">
    <div class="absolute -top-6 left-1/2 transform -translate-x-1/2 bg-purple-500 text-white w-12 h-12 rounded-full flex items-center justify-center text-2xl shadow-md">
      🚀
    </div>
    <div class="mt-6 text-center">
      <h3 class="font-bold text-purple-800 text-lg">น้องมายด์ (พัสดุ)</h3>
      <p class="text-xs text-gray-400">"เติบโต เพราะวิเคราะห์เก่ง"</p>
    </div>
    <div class="mt-4 text-xs text-gray-600 space-y-2 text-left">
      <p>❌ <b>ก่อนหน้า:</b> ทำ Excel ได้แค่พื้นฐาน กลัวผิดพลาด ทำงานตามคำสั่ง</p>
      <p>✅ <b>ใช้ AI:</b> เขียนสูตร Excel ขั้นเทพ + วิเคราะห์แนวโน้มราคาเสนอผู้บริหาร</p>
      <div class="bg-purple-50 p-2 rounded text-purple-700 font-bold text-center mt-2">
        "ผลงานเข้าตา! จากคนทำงานกลายเป็นนักวิเคราะห์"
      </div>
    </div>
  </div>

</div>

---

# 🪄 AI เสกสูตร Excel (Formula Magic) 📊
เลิกจำสูตรยาวๆ... พิมพ์บอกความต้องการไปเลย!

<div class="grid grid-cols-2 gap-8 mt-6">
  <!-- Example 1: แยกชื่อ-นามสกุล -->
  <div class="bg-green-50 p-4 rounded-xl border border-green-200">
     <h3 class="font-bold text-green-800 mb-2">1. แยกชื่อ - นามสกุล</h3>
     <div class="text-[10px] text-gray-500 mb-1">โจทย์: แยก "นายสมชาย ใจดี" ให้อยู่คนละช่อง</div>
     <div class="bg-red-100 p-2 rounded mb-2 opacity-60">
       <b class="text-red-700">มนุษย์ (The Old Way):</b><br>
       <code class="text-[10px] text-red-600">=LEFT(A2, FIND(" ", A2)-1)</code>
     </div>
     <div class="bg-green-100 p-2 rounded shadow-sm">
       <b class="text-green-700">AI Prompt (The New Way):</b><br>
       <p class="text-[10px] italic">"เขียนสูตร Excel แยกข้อความในช่อง A2 โดยเอาเฉพาะคำหน้า ก่อนถึงช่องว่าง"</p>
     </div>
  </div>

  <!-- Example 2: ตัดเกรด -->
  <div class="bg-blue-50 p-4 rounded-xl border border-blue-200">
     <h3 class="font-bold text-blue-800 mb-2">2. ตัดเกรด (Nested IF)</h3>
     <div class="text-[10px] text-gray-500 mb-1">โจทย์: คะแนน >80=A, >70=B, >60=C...</div>
     <div class="bg-red-100 p-2 rounded mb-2 opacity-60">
       <b class="text-red-700">มนุษย์ (Headache):</b><br>
       <code class="text-[10px] text-red-600">=IF(A2>80,"A",IF(A2>70,"B",IF(A2>60,"C","F")))</code>
     </div>
     <div class="bg-green-100 p-2 rounded shadow-sm">
       <b class="text-green-700">AI Prompt:</b><br>
       <p class="text-[10px] italic">"เขียนสูตรตัดเกรดจากช่อง A2 โดยถ้ามากกว่า 80 ได้ A, 70 ได้ B, 60 ได้ C นอกนั้นตก"</p>
     </div>
  </div>

</div>

---

<div class="mt-4 p-4 bg-purple-50 rounded-xl border border-purple-200">
  <h3 class="font-bold text-purple-800 mb-2">3. ข้าม Sheet (VLOOKUP / XLOOKUP) 🚀</h3>
  <div class="flex items-center gap-4">
    <div class="flex-1 text-sm bg-gray-100 p-2 rounded">
      <b>Prompt:</b> "ช่วยเขียนสูตร <b>VLOOKUP</b> ให้หน่อย เอาข้อมูล <b>'ราคาสินค้า'</b> จาก Sheet ชื่อ <b>'PriceList'</b> มาใส่ใน Sheet นี้ โดยอ้างอิงจาก <b>'รหัสสินค้า'</b> ในช่อง <b>A2</b>"
    </div>
    <div class="text-2xl">👉</div>
    <div class="flex-1 bg-white p-2 rounded border border-gray-300 font-mono text-xs text-blue-600 overflow-x-auto">
      =VLOOKUP(A2, 'PriceList'!A:B, 2, FALSE)
    </div>
  </div>
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <!-- Example 4 -->
  <div class="p-4 bg-pink-50 rounded-xl border border-pink-200">
    <h3 class="font-bold text-pink-800 mb-2">4. คำนวณอายุงาน (Date) 🗓️</h3>
    <div class="space-y-2">
      <div class="text-xs bg-white p-2 rounded italic text-gray-600">
        "คำนวณ <b>อายุงาน</b> จากวันเริ่ม (A2) ถึงวันนี้ ขอหน่วย <b>ปี-เดือน</b>"
      </div>
      <div class="font-mono text-[10px] text-pink-600 bg-white p-1 rounded border overflow-x-auto">
        =DATEDIF(A2,TODAY(),"Y")&"ปี "&DATEDIF(A2,TODAY(),"YM")&"ด."
      </div>
    </div>
  </div>

  <!-- Example 5 -->
  <div class="p-4 bg-yellow-50 rounded-xl border border-yellow-200">
    <h3 class="font-bold text-yellow-800 mb-2">5. รวมยอดแบบมีเงื่อนไข (SUMIFS) �</h3>
    <div class="space-y-2">
      <div class="text-xs bg-white p-2 rounded italic text-gray-600">
        "รวมเงิน (Col D) เฉพาะของ <b>'แผนก IT'</b> (Col B) ที่สถานะ <b>'Active'</b> (Col C)"
      </div>
      <div class="font-mono text-[10px] text-yellow-600 bg-white p-1 rounded border overflow-x-auto">
        =SUMIFS(D:D, B:B, "IT", C:C, "Active")
      </div>
    </div>
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

# 3 Steps ในการสร้างคำสั่ง (The 3 Steps)
หัวใจสำคัญ: **Role (บทบาท) + Task (งาน) + Context & Format (บริบทและรูปแบบ)**

<div class="grid grid-cols-3 gap-4 mt-8">
  <div class="bg-blue-50 p-4 rounded-xl border border-blue-200">
    <div class="text-3xl mb-2">🎭</div>
    <b class="text-blue-700">1. Role</b>
    <p class="text-sm mt-2">ระบุตัวตนให้ AI เช่น <br>"รับบทเป็น HR มืออาชีพ...", "รับบทเป็นวิศวกร..."</p>
  </div>
  <div class="bg-yellow-50 p-4 rounded-xl border border-yellow-200">
    <div class="text-3xl mb-2">📝</div>
    <b class="text-yellow-700">2. Task</b>
    <p class="text-sm mt-2">สั่งงานให้ชัดเจน พุ่งเป้า <br>"ร่างจดหมาย...", "สรุปรายงาน...", "เขียนสูตร Excel..."</p>
  </div>
  <div class="bg-green-50 p-4 rounded-xl border border-green-200">
    <div class="text-3xl mb-2">📦</div>
    <b class="text-green-700">3. Format</b>
    <p class="text-sm mt-2">กำหนดหน้าตาผลลัพธ์ <br>"ขอเป็นตาราง", "ขอเป็นข้อๆ", "ขอภาษาที่เป็นทางการ"</p>
  </div>
</div>

---

# Specific Prompt (เจาะจงให้ชัด)
อย่าสั่งกว้างๆ ให้สั่งเหมือนสั่งลูกน้องที่ยังไม่รู้งาน

<div class="grid grid-cols-2 gap-8 mt-6">
  <div class="bg-red-50 p-6 rounded-xl border border-red-200 opacity-70">
    <h3 class="font-bold text-red-700 mb-2">❌ General (กว้างไป)</h3>
    <p class="text-xl">"เขียนอีเมลลางานให้หน่อย"</p>
    <p class="text-sm text-gray-500 mt-4">(AI จะเขียนมาแบบกลางๆ อาจจะไม่ตรงเหตุผลของเรา)</p>
  </div>
  <div class="bg-green-50 p-6 rounded-xl border border-green-200 shadow-lg">
    <h3 class="font-bold text-green-700 mb-2">✅ Specific (เจาะจง)</h3>
    <CopyBox text="เขียนอีเมลลางาน เนื่องจากป่วยเป็นไข้หวัดใหญ่ ขอลา 2 วัน (27-28 ม.ค.) ส่งถึง ผอ.กองอาคารฯ ขอภาษา สุภาพและเป็นทางการ">
      <p class="text-lg">"เขียนอีเมลลางาน <b>เนื่องจากป่วยเป็นไข้หวัดใหญ่</b> ขอลา <b>2 วัน (27-28 ม.ค.)</b> ส่งถึง <b>ผอ.กองอาคารฯ</b> ขอภาษา <b>สุภาพและเป็นทางการ</b>"</p>
    </CopyBox>
  </div>
</div>

---

# Adjusting Prompt (จูงใจให้ได้ผลลัพธ์)
AI คือแชทบอท... **"คุยโต้ตอบได้"** ไม่ต้องเริ่มใหม่ถ้ามันทำผิด

<div class="mt-6 flex flex-col gap-4">
  <CopyBox text="ร่างหนังสือเชิญวิทยากรให้หน่อย">
  <div class="bg-gray-100 p-4 rounded-lg flex items-center gap-4">
    <div class="bg-blue-500 text-white w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0">You</div>
    <div>"ร่างหนังสือเชิญวิทยากรให้หน่อย"</div>
  </div>
  </CopyBox>
  <div class="bg-white border p-4 rounded-lg flex items-center gap-4 ml-8">
     <div class="text-2xl">🤖</div>
     <div class="text-gray-500 italic">(AI ร่างมาให้... แต่มันยาวเกินไป และดูโบราณ)</div>
  </div>
  <CopyBox text="ขอสั้นลงกว่านี้ครึ่งนึง และปรับภาษาให้ทันสมัยขึ้น ไม่เอาคำฟุ่มเฟือย">
  <div class="bg-blue-50 p-4 rounded-lg flex items-center gap-4 border border-blue-200">
    <div class="bg-blue-500 text-white w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0">You</div>
    <div class="font-bold text-blue-800">"ขอสั้นลงกว่านี้ครึ่งนึง และปรับภาษาให้ทันสมัยขึ้น ไม่เอาคำฟุ่มเฟือย"</div>
  </div>
  </CopyBox>
</div>

<div class="mt-4 text-center text-gray-600">
  💡 Tip: สั่งแก้ได้เรื่อยๆ จนกว่าจะพอใจ (Make it shorter, Make it professional, Add emojis)
</div>

---

# Present ให้เห็นภาพ ด้วย AI Analogy
เทคนิคอธิบายเรื่องยากๆ ให้เข้าใจง่าย **"เปรียบเทียบกับสิ่งที่คุ้นเคย"**

<div class="mt-6 p-6 bg-purple-50 rounded-xl border border-purple-200">
  <h3 class="font-bold text-purple-700 text-xl mb-4">🔮 Analogy Prompting</h3>
  <CopyBox text="ช่วยอธิบายเรื่อง [หัวข้อยากๆ] ให้เข้าใจง่ายๆ โดยเปรียบเทียบกับ [เรื่องในชีวิตประจำวัน]">
    <div class="text-lg bg-white p-4 rounded border border-gray-200 font-mono text-gray-700">
      "ช่วยอธิบายเรื่อง <b>[หัวข้อยากๆ]</b> ให้เข้าใจง่ายๆ <br>
      โดยเปรียบเทียบกับ <b>[เรื่องในชีวิตประจำวัน]</b>"
    </div>
  </CopyBox>
  
  <div class="mt-6 grid grid-cols-2 gap-4">
    <div class="bg-white p-3 rounded shadow-sm">
      <b>ตัวอย่าง 1:</b>
      <p class="text-sm mt-1">"อธิบายระบบ <b>Blockchain</b> โดยเปรียบเทียบกับ <b>'ป้าข้างบ้าน'</b>" <br></p>
    </div>
      <div class="bg-white p-3 rounded shadow-sm">
      <b>ตัวอย่าง 2:</b>
      <p class="text-sm mt-1">"อธิบายระบบ <b>ERP</b> โดยเปรียบเทียบกับ <b>'มนุษย์เมีย (ภรรยา)'</b>" <br></p>
    </div>
  </div>
</div>

---

# Framework สร้าง Presentation
ให้ AI ช่วยคิด **"โครงเรื่อง"** ก่อนเริ่มทำสไลด์จริง

<div class="grid grid-cols-2 gap-8 mt-6">
  <div>
     <h3 class="text-xl font-bold mb-2">ทำไมต้องใช้ AI คิดโครง?</h3>
     <ul class="list-disc pl-5 space-y-2 text-gray-700">
       <li>ไม่ตกหล่นประเด็นสำคัญ</li>
       <li>จัดลำดับเรื่องเล่า (Storytelling) ให้น่าสนใจ</li>
       <li>ประหยัดเวลา "กระดาษเปล่า" (Blank Page Syndrome)</li>
     </ul>
  </div>
  <div class="bg-indigo-50 p-5 rounded-xl border border-indigo-200">
     <h3 class="font-bold text-indigo-700 mb-2">🚀 The Prompt</h3>
     <CopyBox text="ช่วยวาง Outline สำหรับ Slide Presentation เรื่อง [รายงานผลการดำเนินงานประจำปี] สำหรับนำเสนอ [คณบดีและผู้บริหาร] จำนวน [10] หน้า เน้นเรื่อง [ความคุ้มค่าและผลสำเร็จ]">
       <p class="font-mono text-sm bg-white p-3 rounded border border-indigo-100">
         "ช่วยวาง Outline สำหรับ Slide Presentation เรื่อง <b>[รายงานผลการดำเนินงานประจำปี]</b> <br>
         สำหรับนำเสนอ <b>[คณบดีและผู้บริหาร]</b> <br>
         จำนวน <b>[10]</b> หน้า <br>
         เน้นเรื่อง <b>[ความคุ้มค่าและผลสำเร็จ]</b>"
       </p>
     </CopyBox>
  </div>
</div>

---

# ทำ Executive Summary (สรุปผู้บริหาร)
เปลี่ยน 'น้ำ' ให้เป็น 'เนื้อ' สำหรับผู้บริหารที่มีเวลาน้อย

<div class="mt-6">
  <div class="bg-orange-50 p-6 rounded-xl border border-orange-200">
    <h3 class="font-bold text-orange-700 mb-4">📝 Summarization Prompt</h3>
    <div class="grid grid-cols-2 gap-8">
      <div class="text-sm">
        <p class="mb-2"><b>Input:</b> (Copy text ยาวๆ หรือ Upload File)</p>
        <p class="mb-4"><b>Prompt:</b></p>
        <CopyBox text="ช่วยสรุปเอกสารนี้แบบ Executive Summary ความยาวไม่เกิน 1 หน้ากระดาษ โดยแยกหัวข้อเป็น: 1. ประเด็นสำคัญ (Key Findings) 2. สิ่งที่ต้องตัดสินใจ (Decisions Needed) 3. งบประมาณที่ใช้ (Budget)">
          <div class="bg-white p-3 rounded border border-orange-100 font-mono text-gray-700">
            "ช่วยสรุปเอกสารนี้แบบ Executive Summary <br>
            ความยาวไม่เกิน <b>1 หน้ากระดาษ</b> <br>
            โดยแยกหัวข้อเป็น: <br>
            1. ประเด็นสำคัญ (Key Findings) <br>
            2. สิ่งที่ต้องตัดสินใจ (Decisions Needed) <br>
            3. งบประมาณที่ใช้ (Budget)"
          </div>
        </CopyBox>
      </div>
      <div class="flex items-center justify-center">
         <div class="text-center">
           <div class="text-6xl mb-2">📑 ➡ 📄</div>
           <p class="text-gray-500">จาก 50 หน้า เหลือ 1 หน้า</p>
         </div>
      </div>
    </div>
  </div>
</div>

---

# สุดยอด AI ช่วยทำสไลด์ (Presentation Tools) 🖥️
"เบื่อทำสไลด์เองใช่ไหม? ให้ AI ช่วยสิ!"

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="bg-indigo-50 p-4 rounded-xl border border-indigo-200">
    <h3 class="font-bold text-indigo-700 mb-2">🚀 สร้างใหม่จากศูนย์ (Text-to-Slide)</h3>
    <p class="text-xs mb-2 text-gray-600">แค่พิมพ์หัวข้อ -> ได้สไลด์ครบชุด</p>
    <ul class="list-disc pl-5 text-sm space-y-1">
      <li><b>Gamma.app:</b> สวย, เร็ว, รองรับภาษาไทยดีเยี่ยม (Top Pick! ⭐)</li>
      <li><b>AIppt:</b> สร้างเนื้อหาอัตโนมัติจาก Prompt</li>
      <li><b>Slidesgo.ai:</b> มี Template พรีเมียมเยอะ</li>
    </ul>
  </div>

  <div class="bg-pink-50 p-4 rounded-xl border border-pink-200">
     <h3 class="font-bold text-pink-700 mb-2">🎨 เน้นดีไซน์สวย (Design Focus)</h3>
     <p class="text-xs mb-2 text-gray-600">จัดวางเลย์เอาต์ให้อัตโนมัติ</p>
     <ul class="list-disc pl-5 text-sm space-y-1">
       <li><b>Beautiful.ai:</b> สไลด์ดูแพง แบบมือโปร (Smart Layouts)</li>
       <li><b>Wonderslide:</b> จัดเรียงเนื้อหาให้สวยงามทันใจ</li>
       <li><b>DesignCap:</b> เน้นทำโปสเตอร์/Infographic ง่ายๆ</li>
     </ul>
  </div>
</div>

---

# AI เสกภาพตกแต่ง (Image Generators) 🖼️
หยุดหาภาพใน Google (ที่อาจติดลิขสิทธิ์)... **"สร้างเองเลย!"**

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="bg-white p-4 rounded-xl shadow-lg border-t-4 border-purple-500">
    <div class="text-3xl mb-2">🦁</div>
    <b class="text-purple-700">Leonardo.ai</b>
    <p class="text-xs mt-2 text-gray-600">คุณภาพสูงมาก สวยระดับสตูดิโอ (สายฟรีใช้ได้เยอะ)</p>
  </div>
  <div class="bg-white p-4 rounded-xl shadow-lg border-t-4 border-pink-500">
    <div class="text-3xl mb-2">🔮</div>
    <b class="text-pink-700">Dream by Wombo</b>
    <p class="text-xs mt-2 text-gray-600">เน้นงานศิลปะ อาร์ตๆ ใช้งานง่ายบนมือถือ</p>
  </div>
  <div class="bg-white p-4 rounded-xl shadow-lg border-t-4 border-blue-500">
    <div class="text-3xl mb-2">🎨</div>
    <b class="text-blue-700">DALL-E 3</b>
    <p class="text-xs mt-2 text-gray-600">ใช้ผ่าน ChatGPT ได้เลย สั่งเป็นภาษาไทยได้</p>
  </div>
</div>
<CopyBox text="ภาพวาดสีน้ำมัน ของแมวใส่สูททางาน ในออฟฟิศสมัยใหม่ แสงอบอุ่น">
<div class="mt-4 text-center text-xs text-gray-500 bg-gray-100 p-2 rounded">
  <b>Prompt Idea:</b> "ภาพวาดสีน้ำมัน ของแมวใส่สูททางาน ในออฟฟิศสมัยใหม่ แสงอบอุ่น"
</div>
</CopyBox>

---

# AI สร้างวิดีโอและเสียง (Video & Voice) 🎬
เพิ่มมูลค่าให้งานนำเสนอ ด้วยสื่อมัลติมีเดียล้ำๆ

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="p-4 border rounded-xl bg-orange-50">
     <h3 class="font-bold text-orange-700 text-lg mb-2">🎥 Text-to-Video</h3>
     <ul class="space-y-2 text-sm">
       <li><b>Lumen5:</b> แปลงบทความ/Blog ให้เป็นวิดีโอ (เหมาะกับทำสื่อการสอน)</li>
       <li><b>Invideo:</b> ตัดต่อวิดีโอออนไลน์ มี Template ให้เลือกเยอะ</li>
       <li><b>Pictory:</b> ตัดคลิปยาวๆ ให้สั้นลงอัตโนมัติ</li>
     </ul>
  </div>
  <div class="p-4 border rounded-xl bg-teal-50">
     <h3 class="font-bold text-teal-700 text-lg mb-2">🎙️ Text-to-Speech (เสียงบรรยาย)</h3>
     <ul class="space-y-2 text-sm">
       <li><b>Murf.ai:</b> เสียงพากย์ AI ที่ "เหมือนคนจริง" ที่สุด (เลือกอารมณ์ได้)</li>
       <li><b>NaturalReader:</b> แปลงข้อความเป็นเสียง อ่านเอกสารให้ฟังฟรีๆ</li>
     </ul>
  </div>
</div>


---

# AI ปรับจูนอารมณ์ (EQ & Professional Tone)
เปลี่ยน "อารมณ์โกรธ" ให้เป็น "ความเป็นมืออาชีพ" (เหมาะกับงานตอบ Complain)

<div class="grid grid-cols-2 gap-8 mt-6">
  <div class="bg-red-50 p-4 rounded-xl border border-red-200 opacity-60">
    <h3 class="font-bold text-red-700 mb-2">🤬 Before (สิ่งที่เราคิด)</h3>
    <p class="italic text-gray-700">"ส่งของช้ามาก! ทำงานกันยังไง? ลูกค้ารอจนหงุดหงิดหมดแล้ว ถ้าทำไม่ได้ก็บอกเลิกสัญญาไปเลย!"</p>
  </div>
  <div class="bg-blue-50 p-4 rounded-xl border border-blue-200 shadow-lg">
    <h3 class="font-bold text-blue-700 mb-2">👔 After (AI ช่วยเกลา)</h3>
    <p class="text-gray-800">"ขอสอบถามสถานะการจัดส่งครับ เนื่องจากลูกค้าเริ่มสอบถามเข้ามา ขอกำหนดการที่ชัดเจนเพื่อแจ้งลูกค้าครับ (หากติดขัดตรงไหนแจ้งได้เลยนะครับ)"</p>
  </div>
</div>
<CopyBox text="ช่วยปรับข้อความนี้ให้ดู Suffer (สุภาพ), Professional (มืออาชีพ) และมี Empathy (เห็นอกเห็นใจ)">
  <div class="mt-4 text-center bg-gray-100 p-2 rounded text-sm text-gray-600">
    <b>Prompt:</b> "ช่วยปรับข้อความนี้ให้ดู <b>Suffer (สุภาพ)</b>, <b>Professional (มืออาชีพ)</b> และมี <b>Empathy (เห็นอกเห็นใจ)</b>"
  </div>
</CopyBox>

---

# งานวิจัยและค้นหาข้อมูล (Perplexity)
ลืมพฤติกรรม "ถาม ChatGPT แล้วเชื่อเลย" ไปซะ... ถ้าอยากได้ Fact ต้อง Perplexity

<div class="grid grid-cols-2 gap-6 mt-6">
  <div>
    <h3 class="text-xl font-bold mb-3">ทำไม ChatGPT ถึงไม่พอ?</h3>
    <ul class="list-disc pl-5 space-y-2 text-gray-700 text-sm">
      <li>ChatGPT อาจจะ "มั่ว" (Hallucination) ถ้าไม่มีข้อมูล</li>
      <li>ข้อมูลอาจจะเก่า (ไม่อัปเดต Real-time เท่า Google)</li>
    </ul>
    <div class="mt-4 p-4 bg-teal-50 border border-teal-200 rounded-xl">
       <b class="text-teal-700">✅ Solution: Perplexity.ai</b>
       <p class="text-xs mt-1">มันคือ "Google Search + AI Summary" <br>ค้นหาข้อมูลจริง + สรุปให้ + <b>แนบอ้างอิงให้กดเช็ค</b></p>
    </div>
  </div>
  <div class="flex items-center justify-center p-4">
     <div class="text-center">
        <span class="text-8xl">🔎</span>
        <p class="mt-2 text-gray-400">"Trust, but Verify"</p>
     </div>
  </div>
</div>

---

# โครงสร้าง AIDA (สำหรับงาน PR)
เขียนประกาศ/ข่าวประชาสัมพันธ์ ให้น่าอ่านและ "มีคนกด"

<div class="mt-6 p-6 bg-yellow-50 rounded-xl border border-yellow-200">
  <h3 class="font-bold text-yellow-800 mb-4">📢 Prompt สูตรการตลาด (AIDA Model)</h3>
  <!-- ... grid ... -->
  <div class="grid grid-cols-4 gap-2 text-center text-xs">
    <div class="bg-white p-2 rounded border shadow-sm">
      <b class="block text-red-600 text-lg">A</b>ttention<br>(ดึงความสนใจ)
    </div>
    <div class="bg-white p-2 rounded border shadow-sm">
      <b class="block text-orange-600 text-lg">I</b>nterest<br>(ให้ข้อมูลน่ารู้)
    </div>
    <div class="bg-white p-2 rounded border shadow-sm">
      <b class="block text-blue-600 text-lg">D</b>esire<br>(กระตุ้นความอยาก)
    </div>
    <div class="bg-white p-2 rounded border shadow-sm">
      <b class="block text-green-600 text-lg">A</b>ction<br>(บอกให้ทำอะไร)
    </div>
  </div>
  <CopyBox text="ช่วยเขียน [ประกาศรับสมัครงาน] โดยใช้โครงสร้าง AIDA Framework เพื่อให้ดูท้าทายและน่าตื่นเต้น สำหรับคนรุ่นใหม่">
    <div class="mt-4 bg-white p-3 rounded font-mono text-gray-700 text-sm">
      "ช่วยเขียน <b>[ประกาศรับสมัครงาน]</b> โดยใช้โครงสร้าง <b>AIDA Framework</b> <br>
      เพื่อให้ดูท้าทายและน่าตื่นเต้น สำหรับคนรุ่นใหม่"
    </div>
  </CopyBox>
</div>

---

# ข้อควรระวัง (Do's & Don'ts) 🛡️
AI ฉลาด... แต่เราต้องฉลาดกว่าเรื่อง "ความปลอดภัย"

<div class="grid grid-cols-3 gap-4 mt-8">
  <div class="bg-red-50 p-4 rounded-xl border-t-4 border-red-500 text-center">
    <div class="text-4xl mb-2">🚫</div>
    <h3 class="font-bold text-red-700">ความลับห้ามใส่</h3>
    <p class="text-xs mt-2 text-gray-600">รหัสผ่าน, เงินเดือน, ข้อมูลส่วนตัวนิสิต/อาจารย์ <br>(ถือว่า Upload ขึ้น Server เขา)</p>
  </div>
  <div class="bg-yellow-50 p-4 rounded-xl border-t-4 border-yellow-500 text-center">
    <div class="text-4xl mb-2">🤥</div>
    <h3 class="font-bold text-yellow-700">อย่าเชื่อ 100%</h3>
    <p class="text-xs mt-2 text-gray-600">AI มั่วได้ (Hallucination) <br>ต้องตรวจทาน (Verify) เสมอ ก่อนส่งนาย</p>
  </div>
  <div class="bg-green-50 p-4 rounded-xl border-t-4 border-green-500 text-center">
    <div class="text-4xl mb-2">⚖️</div>
    <h3 class="font-bold text-green-700">ลิขสิทธิ์</h3>
    <p class="text-xs mt-2 text-gray-600">ภาพที่ AI สร้าง ปัจจุบันยัง <br>"จดลิขสิทธิ์ไม่ได้" (Public Domain)</p>
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
      <li><b>Task 1:</b> ร่าง "บันทึกข้อความขออนุมัติโครงการ" (International AI Seminar)</li>
      <li><b>Task 2:</b> ร่าง "อีเมลเชิญวิทยากร" (ต่อเนื่องจากโครงการตะกี้)</li>
    </ul>
    <div class="mt-4 space-y-2">
      <div class="flex items-center gap-2 text-[10px] text-gray-500">
        <span class="bg-blue-100 text-blue-800 px-1 rounded font-bold">Step 1</span> ขออนุมัติจัดโครงการ:
      </div>
      <CopyBox text="ช่วยร่างบันทึกข้อความ 'ขออนุมัติจัดโครงการสัมมนา International AI Seminar 2026' เพื่อยกระดับความเป็นนานาชาติ งบประมาณ 50,000 บาท เรียน คณบดี ขอภาษาทางการถูกต้องตามระเบียบงานสารบรรณ">
        <div class="bg-gray-100 p-2 rounded text-xs border border-gray-200">
          <b>Prompt (Memo):</b> "ร่างบันทึกข้อความขออนุมัติโครงการ International AI Seminar..."
        </div>
      </CopyBox>
      <div class="flex items-center gap-2 text-[10px] text-gray-500 mt-1">
        <span class="bg-blue-100 text-blue-800 px-1 rounded font-bold">Step 2</span> เชิญวิทยากร (ต่อเนื่อง):
      </div>
      <CopyBox text="จากโครงการในข้อเมื่อกี้ ช่วยร่างอีเมลเชิญ Prof. Hiroshi Tanaka (University of Tokyo) มาเป็น Keynote Speaker ในหัวข้อ 'AI for Future Administration' โดยทางเราจะออกค่าตั๋วเครื่องบินและที่พักให้ ขอภาษา Business English">
        <div class="bg-blue-50 p-2 rounded text-xs border border-blue-200">
          <b>Prompt (Email):</b> "จากโครงการตะกี้... ช่วยร่างอีเมลเชิญ Prof. Hiroshi Tanaka..."
        </div>
      </CopyBox>
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
      <li><b>Challenge:</b> สร้างคลิปวิดีโอ "คนพูดประกาศ" จากรูปถ่าย (Avatar)</li>
    </ul>
    <div class="mt-4 space-y-2">
      <div class="flex items-center gap-2 text-[10px] text-gray-500">
        <span class="bg-green-100 text-green-800 px-1 rounded font-bold">ChatGPT</span> ทำร่างประกาศ:
      </div>
      <CopyBox text="ร่างประกาศปิดปรับปรุงห้องน้ำ... ขอสไตล์ 'ขออภัยในความไม่สะดวก' และแนะนำห้องน้ำใกล้เคียง พร้อมอีโมจิ 🙏">
        <div class="bg-gray-100 p-2 rounded text-xs border border-gray-200">
          <b>1. Prompt (Text):</b> "ร่างประกาศปิดปรับปรุงห้องน้ำ... เพื่อติดบอร์ดประกาศ"
        </div>
      </CopyBox>
      <div class="flex items-center gap-2 text-[10px] text-gray-500 mt-1">
        <span class="bg-green-100 text-green-800 px-1 rounded font-bold">ChatGPT</span> แปลงเป็นบทพูด:
      </div>
      <CopyBox text="ช่วยแปลงประกาศนี้ ให้เป็น 'บทพูดสำหรับถ่ายวิดีโอสั้น' (30 วินาที) ขอภาษาพูดที่ดูเป็นกันเองและจริงใจ เพื่อให้ AI Avatar พูด">
        <div class="bg-blue-50 p-2 rounded text-xs border border-blue-200">
          <b>2. Prompt (Video Script):</b> "ช่วยแปลงประกาศนี้ เป็นบทพูดสำหรับ AI Avatar"
        </div>
      </CopyBox>
      <div class="mt-2 text-[10px] bg-purple-100 text-purple-800 p-2 rounded flex items-center justify-between border border-purple-200">
         <span>🎥 <b>Next Step:</b> นำบทพูดไปใส่ใน <b>HeyGen / D-ID</b> เพื่อสร้างคลิป</span>
         <span class="text-xl">👉</span>
      </div>
    </div>
  </div>
  <div class="flex items-center justify-center bg-yellow-50 rounded-xl">
    <span class="text-6xl">🚧</span>
  </div>
</div>

---

# 🔮 Demo 3: งานคลัง & ระเบียบ (Ask PDF)
**Scenario:** ถาม-ตอบ "ข้อมูลในระเบียบ/คู่มือ" (ไม่อยากอ่านเองทั้งเล่ม)

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <h3 class="font-bold text-green-600">โจทย์จริง:</h3>
    <ul class="list-disc pl-5 text-sm space-y-2">
      <li>มีไฟล์ PDF "ระเบียบการเบิกจ่ายฯ" หนา 100 หน้า</li>
      <li>อยากรู้แค่ <b>"ค่าที่พักเบิกได้เท่าไหร่?"</b> ขี้เกียจเปิดหา</li>
    </ul>
    <div class="mt-4 bg-gray-100 p-2 rounded text-xs">
      <b>Action:</b> Upload PDF ให้ AI -> แล้วถามเจาะจงเลย
      <CopyBox text="ช่วยสรุปเกณฑ์การเบิก 'ค่าเช่าที่พัก' สำหรับพนักงานสายสนับสนุน ว่าเบิกได้คืนละกี่บาท และต้องใช้หลักฐานอะไรบ้าง">
      <i>"ช่วยสรุปเกณฑ์การเบิก 'ค่าเช่าที่พัก' สำหรับพนักงานสายสนับสนุน <br>
      ว่าเบิกได้คืนละกี่บาท และต้องใช้หลักฐานอะไรบ้าง"</i>
      </CopyBox>
    </div>
  </div>
  <div class="flex flex-col items-center justify-center bg-green-50 rounded-xl p-2">
    <div class="text-4xl mb-2">📑</div>
    <div class="text-[10px] text-gray-400 bg-white p-2 rounded border text-center">
      (File: ระเบียบการเบิกจ่าย.pdf) <br>
      <span class="text-green-600">Chat with PDF</span>
    </div>
  </div>
</div>

---

# 🔮 Demo 4: ศูนย์คอมฯ & PR (Special Request)
**Scenario:** ทำ Infographic จากกำหนดการ

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <h3 class="font-bold text-purple-600">โจทย์พิเศษ:</h3>
    <ul class="list-disc pl-5 text-sm space-y-2">
      <li>"นำกำหนดการสัมมนา (ไฟล์ PDF) ให้ AI สร้างเป็น Infographic"</li>
      <li><b>Problem:</b> ไฟล์เป็น PDF รูปภาพ/ตาราง AI บางตัวอ่านยาก ต้องแกะเป็น Text ก่อน</li>
    </ul>
    <div class="mt-4 space-y-2">
       <div class="flex items-center gap-2 text-[10px] text-gray-500">
        <span class="bg-green-100 text-green-800 px-1 rounded font-bold">Step 1</span> แปลง PDF เป็น Text:
      </div>
      <CopyBox text="ช่วยดึงข้อความจากไฟล์ PDF นี้ แล้วสรุปเป็นหัวข้อสั้นๆ สำหรับนำไปทำ Infographic ให้หน่อย">
        <div class="bg-gray-100 p-2 rounded text-xs border border-gray-200">
          <b>Prompt (OCR):</b> "ช่วยดึงข้อความจากไฟล์ PDF แล้วสรุปเป็นหัวข้อสั้นๆ..."
        </div>
      </CopyBox>
    </div>
    <div class="mt-2 text-[10px] bg-purple-100 text-purple-800 p-2 rounded flex items-center justify-between border border-purple-200">
         <span>🎨 <b>Step 2:</b> นำ Text ที่ได้ไปใส่ <b>Piktochart AI</b> (แนะนำตัวนี้! ⭐)</span>
         <span class="text-xl">👉</span>
    </div>
  </div>
  <div class="flex items-center justify-center bg-purple-50 rounded-xl">
    <span class="text-6xl">🎨</span>
  </div>
</div>

---

# 🔮 Demo 5: งานพัสดุ & จัดซื้อ (Price Tracking)
**Scenario:** เปรียบเทียบราคาวัสดุย้อนหลัง 4 เดือน (M9-M12) หาตัวที่ "แพงขึ้น"

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <h3 class="font-bold text-red-600">โจทย์จริง (Price Reports):</h3>
    <ul class="list-disc pl-5 text-sm space-y-2">
      <li>มีไฟล์ Excel 4 ไฟล์ (ก.ย. - ธ.ค.) เก็บราคาวัสดุ</li>
      <li>ต้องการรู้ว่า <b>"รายการไหนมีการปรับราคาขึ้น?"</b> และ <b>"ขึ้นกี่บาท?"</b></li>
      <li>(ถ้าทำมือ ต้องเปิดเทียบทีละไฟล์ ตาลายแน่นอน!)</li>
    </ul>
    <div class="mt-4 bg-gray-100 p-2 rounded text-xs">
      <b>Action:</b> Upload ไฟล์ M9, M10, M11, M12 พร้อมกันแล้วถาม
      <CopyBox text="ช่วยเปรียบเทียบราคาวัสดุจาก 4 ไฟล์นี้ (M9-M12) สร้างตารางสรุปรายการที่มีการ 'ปรับราคาขึ้น' และคำนวณ % การเปลี่ยนแปลงให้ด้วย">
      <i>"ช่วยเปรียบเทียบราคาวัสดุจาก 4 ไฟล์นี้ (M9-M12) <br>
      สร้างตารางสรุปรายการที่มีการ <b>'ปรับราคาขึ้น'</b> <br>
      และคำนวณ % การเปลี่ยนแปลงให้ด้วย"</i>
      </CopyBox>
    </div>
  </div>
  <div class="flex flex-col items-center justify-center bg-red-50 rounded-xl p-2">
    <div class="text-4xl mb-2">📈</div>
    <div class="text-[10px] text-gray-400 bg-white p-2 rounded border text-center">
      (File: Price_Report M9-M12.xlsx) <br>
      <span class="text-green-600">Excel Analysis 101</span>
    </div>
  </div>
</div>

---
layout: center
class: text-center
---

# 🛠️ เครื่องมือช่วยชีวิต: Engineering AI Prompter
(แจกฟรี! Web App ที่ทำมาเพื่อพวกเราโดยเฉพาะ)

<div class="mt-4 flex justify-center">
  <div class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-6 rounded-2xl shadow-xl max-w-4xl flex items-center gap-8">
    <div class="flex-1 text-left">
      <h2 class="text-2xl font-bold mb-4">Web App รวมสูตรสำเร็จ</h2>
      <p class="mb-4 text-blue-100 text-sm">
        รวม 16 สถานการณ์ (ธุรการ, พัสดุ, อาคาร, คอมฯ ครบ!)<br>
        แค่เลือก -> เติมคำ -> กด Copy -> ใช้ได้เลย!
      </p>
      <a href="https://script.google.com/macros/s/AKfycbyF-DEUCV60wUqzKYLwLmFvoUC-PUhDPsPpwygDC4H1XscyYz66kWwhGwcliqNhk5CY/exec" target="_blank" class="text-sm text-yellow-300 underline hover:text-white mb-2 block">
        🔗 Link: Engineering AI Prompter
      </a>
      <div class="text-xs bg-white/20 p-2 rounded mt-2 inline-block">
        (สแกน QR Code หรือเข้าลิงค์ได้เลยครับ)
      </div>
    </div>
    <div class="bg-white p-3 rounded-xl flex-shrink-0">
      <img src="/qrcode_webapp.png" class="w-40 h-40" alt="QR Code">
    </div>
  </div>
</div>

---
layout: cover
background: https://source.unsplash.com/random/1920x1080/?coffee,break
---

# พักรับประทานอาหารว่าง
(14.30 - 14.45 น.)
พักผ่อน 15 นาที แล้วกลับมาลุยต่อช่วงสุดท้ายครับ!

---
layout: section
---

# Part 2: Workshop
(14.45 - 16.15 น.)
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

<div class="mt-8 text-sm opacity-50">
  (สไลด์นี้ก็ช่วยสร้างโดย AI : Slidev + Gemini) 🤖
</div>
