---
theme: seriph
title: Generative AI for Work
info: |
  ## Generative AI มาประยุกต์ใช้ในการทำงาน
  โครงการสัมมนาบุคลากรสายสนับสนุนวิชาการ ระดับภาควิชาฯ
  คณะวิศวกรรมศาสตร์ — โดย ผศ.ดร.รุสลี่ สุทธวีร์กูล
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
fonts:
  sans: "Kanit"
  serif: "Sarabun"
  mono: "Fira Code"
layout: cover
background: https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=1920
---

# Generative & Agentic AI

## ยกระดับงานสายสนับสนุนภาควิชาฯ ด้วย AI ยุคใหม่

<div class="mt-6 text-sm opacity-90">
  โดย ผศ.ดร.รุสลี่ สุทธวีร์กูล · ผู้ช่วยคณบดีฝ่ายสารสนเทศ<br/>
  คณะวิศวกรรมศาสตร์ มจพ.
</div>

<div class="absolute bottom-8 left-8 flex items-center gap-3">
  <img src="/logo_eng.jpg" class="w-14 h-14 rounded-full shadow-lg border-2 border-white/60" />
</div>

<div class="absolute bottom-8 right-8 text-center">
  <img src="/qrcode_slides.png" class="w-20 h-20 rounded-lg shadow-lg border-2 border-white/60" />
  <div class="text-[9px] opacity-70 mt-1">Scan Slides</div>
</div>

---
layout: center
class: "!px-16"
---

# 🗺️ แผนการเดินทางวันนี้

<div class="grid grid-cols-2 gap-6 mt-8">

  <div class="rounded-2xl bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-200/60 p-6 text-left shadow-sm">
    <div class="flex items-center gap-2 mb-3">
      <span class="px-2 py-1 bg-blue-600 text-white text-[10px] rounded-full font-bold">PART 1</span>
      <span class="text-xs text-gray-500">09:00 – 10:30</span>
    </div>
    <h3 class="text-lg font-bold text-blue-900 mb-3">บรรยาย &amp; สาธิตสด</h3>
    <ul class="text-sm text-gray-700 space-y-1.5">
      <li>🌱 วิวัฒนาการ AI: Chat → Gen → Agentic</li>
      <li>✨ เทียบ 3 ค่ายใหญ่ (ChatGPT / Claude / Gemini)</li>
      <li>🤖 Agentic AI — ลูกน้องที่ "ทำเอง" ได้</li>
      <li>🎯 Prompt Engineering ฉบับทำงานจริง</li>
      <li>🔮 Live Demo 5 เคส ตรงงานภาควิชา</li>
    </ul>
  </div>

  <div class="rounded-2xl bg-gradient-to-br from-amber-50 to-pink-50 border border-amber-200/60 p-6 text-left shadow-sm">
    <div class="flex items-center gap-2 mb-3">
      <span class="px-2 py-1 bg-amber-600 text-white text-[10px] rounded-full font-bold">PART 2</span>
      <span class="text-xs text-gray-500">10:45 – 12:00</span>
    </div>
    <h3 class="text-lg font-bold text-amber-900 mb-3">Workshop ลงมือทำ</h3>
    <ul class="text-sm text-gray-700 space-y-1.5">
      <li>🛠️ แจก Web App "Engineering AI Prompter"</li>
      <li>💻 ลองสร้าง Prompt เพื่อใช้กับงานจริงของตัวเอง</li>
      <li>🙋 ถาม-ตอบ และแก้ไขปัญหาไปพร้อมกัน</li>
      <li>🌟 แชร์ไอเดียเด็ดๆ เพื่อนำไปปรับใช้</li>
    </ul>
  </div>

</div>

<div class="mt-6 text-center text-xs text-gray-500 italic">
  "วันนี้เน้นสนุก · ใช้งานได้จริง · กลับไปเริ่มใช้พรุ่งนี้ได้เลย"
</div>

---
layout: center
---

# 📣 เสียงจากหน้างาน
## (อ้างอิงแบบสอบถามจากสายสนับสนุนระดับคณะฯ)

<div class="text-sm text-gray-500 mb-6">ถึงจะอยู่คนละส่วนงานกัน แต่ปัญหาหน้างานมีความคล้ายคลึงกันมาก...</div>

<div class="grid grid-cols-2 gap-6 text-left">
  <div class="rounded-2xl bg-white border border-blue-100 p-6 shadow-sm relative overflow-hidden">
    <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-blue-500 to-cyan-500"></div>
    <h3 class="text-base font-bold text-blue-800 mb-3">🏆 Top ปัญหาที่อยากได้ผู้ช่วย</h3>
    <ul class="space-y-2 text-sm text-gray-700">
      <li class="flex gap-2"><span class="font-bold text-blue-600">#1</span> ร่าง/แก้หนังสือราชการ &amp; แปลภาษา</li>
      <li class="flex gap-2"><span class="font-bold text-blue-600">#2</span> จัดการสูตร Excel &amp; จัดระเบียบข้อมูล</li>
      <li class="flex gap-2"><span class="font-bold text-blue-600">#3</span> งานประกาศ/โปรโมตข่าวสารต่างๆ</li>
      <li class="flex gap-2"><span class="font-bold text-blue-600">#4</span> สรุปเอกสาร/ระเบียบข้อบังคับด่วน</li>
    </ul>
  </div>

  <div class="rounded-2xl bg-white border border-emerald-100 p-6 shadow-sm relative overflow-hidden">
    <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-emerald-500 to-teal-500"></div>
    <h3 class="text-base font-bold text-emerald-800 mb-3">🥰 สิ่งที่คาดหวังจากสัมมนา</h3>
    <div class="bg-emerald-50 rounded-xl p-3 text-sm text-gray-700 italic leading-relaxed">
      "ไม่เครียด" · "ใช้งานได้จริงทันที" <br>
      "ช่วยลดงานซ้ำซ้อน" · "ไม่วิชาการจ๋า"
    </div>
    <div class="mt-3 text-xs font-semibold text-emerald-700 flex items-center gap-1">
      ✅ รับทราบครับ — วันนี้เจาะจงลุยเคสจริงของภาควิชาฯ
    </div>
  </div>
</div>

---
layout: section
---

# Chapter 1
## วิวัฒนาการของ AI
### จากเครื่องจักรคำนวณ → ลูกน้องดิจิทัล

<div class="mt-6 text-sm opacity-70">รู้ "ที่มา" เพื่อเข้าใจ "ที่ไป"</div>

---

# 🕰️ 3 ยุคของ AI ที่พวกเราต้องรู้

<div class="relative mt-8">
  <div class="absolute top-12 left-0 right-0 h-0.5 bg-gradient-to-r from-gray-300 via-indigo-400 to-pink-500"></div>

  <div class="grid grid-cols-3 gap-6 relative">
    <div v-click class="text-center">
      <div class="w-24 h-24 mx-auto rounded-full bg-gradient-to-br from-gray-200 to-gray-300 flex items-center justify-center text-3xl shadow-md border-4 border-white">💬</div>
      <div class="text-[10px] text-gray-400 mt-2 tracking-widest">~2015–2022</div>
      <h3 class="font-bold text-gray-700 mt-1">AI Chatbot</h3>
      <div class="mt-3 text-xs text-gray-600 bg-gray-50 rounded-xl p-3 text-left">
        <b>รูปแบบ:</b> กล่อง Q&amp;A<br>
        <b>ความสามารถ:</b> ตอบตามสคริปต์/Rule<br>
        <b>เหมือน:</b> "พนักงาน Call Center มือใหม่"
      </div>
    </div>
    <div v-click class="text-center">
      <div class="w-24 h-24 mx-auto rounded-full bg-gradient-to-br from-indigo-400 to-purple-500 flex items-center justify-center text-3xl shadow-lg border-4 border-white">✨</div>
      <div class="text-[10px] text-indigo-500 mt-2 tracking-widest">2022–2024</div>
      <h3 class="font-bold text-indigo-700 mt-1">Generative AI</h3>
      <div class="mt-3 text-xs text-gray-700 bg-indigo-50 rounded-xl p-3 text-left">
        <b>รูปแบบ:</b> คุย + สร้างของ<br>
        <b>ความสามารถ:</b> เขียน/แปล/วาด/สรุป<br>
        <b>เหมือน:</b> "เลขาฯ เก่งหลายภาษา"
      </div>
    </div>
    <div v-click class="text-center">
      <div class="w-24 h-24 mx-auto rounded-full bg-gradient-to-br from-pink-500 to-orange-500 flex items-center justify-center text-3xl shadow-lg border-4 border-white animate-pulse">🤖</div>
      <div class="text-[10px] text-pink-500 mt-2 tracking-widest">2024–ปัจจุบัน</div>
      <h3 class="font-bold text-pink-700 mt-1">Agentic AI</h3>
      <div class="mt-3 text-xs text-gray-700 bg-pink-50 rounded-xl p-3 text-left">
        <b>รูปแบบ:</b> สั่ง 1 ครั้ง ทำต่อเอง<br>
        <b>ความสามารถ:</b> วางแผน + ใช้เครื่องมือ<br>
        <b>เหมือน:</b> "ลูกน้องที่รับผิดชอบงาน"
      </div>
    </div>
  </div>
</div>

<div v-click class="mt-8 text-center text-sm text-gray-500">
  พวกเราส่วนใหญ่ "แตะ" แค่ยุค 2 แล้ว · <b class="text-pink-600">วันนี้จะพาไปยุค 3</b>
</div>

---

# 💡 ต่างกันตรงไหน? ดูตัวอย่างงานเดียวกัน

<div class="text-sm text-gray-500 mb-4">โจทย์: "ขอสรุปรายงานการประชุมครั้งที่แล้ว พร้อมส่งเมลแจ้งอาจารย์ในภาค"</div>

<div class="space-y-3">
  <div class="rounded-xl border border-gray-200 p-4 bg-gray-50 flex items-start gap-4">
    <div class="w-16 text-center">
      <div class="text-2xl">💬</div>
      <div class="text-[10px] font-bold text-gray-500 mt-1">CHATBOT</div>
    </div>
    <div class="flex-1 text-sm">
      ตอบเป็น FAQ ได้ ถ้าคำถามไม่ตรงสคริปต์ = <span class="text-red-500">"ขออภัย ฉันไม่เข้าใจคำถาม"</span>
    </div>
  </div>

  <div class="rounded-xl border border-indigo-200 p-4 bg-indigo-50 flex items-start gap-4">
    <div class="w-16 text-center">
      <div class="text-2xl">✨</div>
      <div class="text-[10px] font-bold text-indigo-600 mt-1">GEN AI</div>
    </div>
    <div class="flex-1 text-sm">
      <b>เรา</b> Copy เนื้อหาประชุม → AI สรุปให้ → <b>เรา</b> Copy ไปวางในเมล → <b>เรา</b> ใส่รายชื่ออาจารย์เอง → <b>เรา</b> กดส่งเอง
      <div class="text-xs text-indigo-600 mt-1">→ "ผู้ช่วยที่เก่ง แต่ต้องจูงมือตลอด"</div>
    </div>
  </div>

  <div class="rounded-xl border-2 border-pink-300 p-4 bg-gradient-to-r from-pink-50 to-orange-50 flex items-start gap-4 shadow-md">
    <div class="w-16 text-center">
      <div class="text-2xl">🤖</div>
      <div class="text-[10px] font-bold text-pink-600 mt-1">AGENTIC</div>
    </div>
    <div class="flex-1 text-sm">
      <b>เราสั่งครั้งเดียว</b> → AI เปิดไฟล์ประชุมใน Drive เอง → สรุป → ดึงรายชื่ออาจารย์จากระบบ → ร่างเมล → <b>รอเราอนุมัติแล้วส่งให้</b>
      <div class="text-xs text-pink-600 mt-1 font-bold">→ "ลูกน้องที่รับผิดชอบงานตั้งแต่ต้นจนจบ" ⚡</div>
    </div>
  </div>
</div>

---
layout: section
---

# Chapter 2
## Generative AI
### ก้าวแรกสู่การทำงานอัตโนมัติ

<div class="mt-6 text-sm opacity-70">ทำความรู้จัก "เลขาฯ ดิจิทัล" ของคุณ</div>

---
layout: center
class: "text-center"
---

<div class="text-xs tracking-[0.3em] uppercase text-pink-400 mb-4">✨ WOW MOMENT #1</div>

# ในห้องนี้... มีผู้ช่วย 1 คน
## ที่ <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-pink-600">ไม่ป่วย ไม่ลา ไม่บ่น</span>

<div class="mt-6 text-gray-600 text-lg">
  ทำงานได้ 24 ชม. · ภาษาไทยเป๊ะ · ค่าจ้าง ~700 บาท/เดือน
</div>

<div class="mt-8 grid grid-cols-4 gap-4 text-center">
  <div><div class="text-3xl font-bold text-indigo-600">0</div><div class="text-xs text-gray-500">วันลา</div></div>
  <div><div class="text-3xl font-bold text-indigo-600">24/7</div><div class="text-xs text-gray-500">ออนไลน์</div></div>
  <div><div class="text-3xl font-bold text-indigo-600">100+</div><div class="text-xs text-gray-500">ภาษา</div></div>
  <div><div class="text-3xl font-bold text-pink-600">฿23/วัน</div><div class="text-xs text-gray-500">ค่าตัว</div></div>
</div>

<div class="mt-8 text-sm text-gray-400 italic">
  คำถามคือ... เราจะใช้เค้ายังไงให้คุ้ม?
</div>

---

# 🧠 Gen AI คืออะไร? (ฉบับภาควิชาฯ)

<div class="text-sm text-gray-500 mb-6">คิดง่ายๆ ว่ามันคือ "น้องใหม่" ที่...</div>

<div class="grid grid-cols-3 gap-5">
  <div v-click class="group">
    <div class="rounded-2xl bg-white border border-gray-200 p-6 hover:border-blue-400 hover:shadow-lg transition-all">
      <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center text-2xl mb-3">📚</div>
      <h3 class="font-bold text-gray-800">อ่านเก่ง</h3>
      <p class="text-xs text-gray-500 mt-2">อ่านระเบียบพัสดุ 100 หน้า สรุปประเด็นสำคัญใน 30 วินาที</p>
    </div>
  </div>
  <div v-click class="group">
    <div class="rounded-2xl bg-white border border-gray-200 p-6 hover:border-purple-400 hover:shadow-lg transition-all">
      <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-2xl mb-3">✍️</div>
      <h3 class="font-bold text-gray-800">เขียนเก่ง</h3>
      <p class="text-xs text-gray-500 mt-2">ร่างบันทึกข้อความ · แปลอีเมลภาษาอังกฤษระดับมืออาชีพ</p>
    </div>
  </div>
  <div v-click class="group">
    <div class="rounded-2xl bg-white border border-gray-200 p-6 hover:border-amber-400 hover:shadow-lg transition-all">
      <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-amber-500 to-orange-500 flex items-center justify-center text-2xl mb-3">💡</div>
      <h3 class="font-bold text-gray-800">คิดเก่ง</h3>
      <p class="text-xs text-gray-500 mt-2">ช่วยวิเคราะห์ข้อมูล · เสนอไอเดีย · ตรวจความถูกต้อง</p>
    </div>
  </div>
</div>

<div v-click class="mt-6 rounded-xl bg-gradient-to-r from-indigo-50 to-purple-50 border border-indigo-100 p-4 text-sm text-gray-700 text-center">
  💎 <b>จุดสำคัญ:</b> Gen AI ไม่ใช่ "Search Engine" แต่คือ <b>"เพื่อนร่วมงานที่ช่วยคิด"</b>
</div>

---

# 🥊 3 ค่ายใหญ่ ณ ปี 2026

<div class="text-sm text-gray-500 mb-4">เลือกให้ถูกโฉลก · งานเร็วขึ้น 3 เท่า</div>

<div class="grid grid-cols-3 gap-3">

  <div class="rounded-2xl bg-white border border-emerald-200 overflow-hidden shadow-sm">
    <div class="h-1 bg-gradient-to-r from-emerald-500 to-teal-500"></div>
    <div class="p-4">
      <div class="flex items-center gap-2 mb-2">
        <div class="w-8 h-8 rounded-lg bg-emerald-500 text-white flex items-center justify-center font-bold">G</div>
        <div>
          <div class="font-bold text-emerald-800 text-sm">ChatGPT</div>
          <div class="text-[9px] text-gray-500">OpenAI · GPT-5</div>
        </div>
      </div>
      <div class="text-[10px] space-y-1.5 text-gray-700">
        <div>✅ ใช้งานทั่วไป รอบรู้หลากหลาย</div>
        <div>✅ ภาษาไทยลื่นไหล ใกล้เคียงมนุษย์</div>
        <div>✅ Voice: คุยด้วยเสียงแบบธรรมชาติ</div>
        <div>✅ สร้างรูปภาพ/อินโฟกราฟิกจากข้อความ</div>
        <div>✅ GPTs: สร้างผู้ช่วยเฉพาะงานของคุณ</div>
      </div>
      <div class="mt-3 rounded-lg bg-emerald-50 p-2 text-[10px]">
        <b class="text-emerald-700">Go ~฿235/เดือน · Plus ~฿700/เดือน ($20)</b><br>
        <span class="text-gray-600">เหมาะ: ใช้งานทั่วไป · ภาษาไทย · Voice/รูปภาพ</span>
      </div>
    </div>
  </div>

  <div class="rounded-2xl bg-white border-2 border-orange-300 overflow-hidden shadow-md relative">
    <div class="absolute top-2 right-2 bg-orange-500 text-white text-[9px] px-2 py-0.5 rounded-full font-bold">⭐ Best Office</div>
    <div class="h-1 bg-gradient-to-r from-orange-500 to-red-500"></div>
    <div class="p-4">
      <div class="flex items-center gap-2 mb-2">
        <div class="w-8 h-8 rounded-lg bg-orange-500 text-white flex items-center justify-center font-bold">C</div>
        <div>
          <div class="font-bold text-orange-800 text-sm">Claude</div>
          <div class="text-[9px] text-gray-500">Anthropic · Opus 4.7</div>
        </div>
      </div>
      <div class="text-[10px] space-y-1.5 text-gray-700">
        <div>✅ Word: ร่างหนังสือราชการ/บันทึกข้อความ</div>
        <div>✅ Excel: ตารางพัสดุ/งบประมาณ + สูตร/Pivot</div>
        <div>✅ PowerPoint: สไลด์รายงาน/นำเสนอ</div>
        <div>✅ Co-work: Projects/Artifacts ทำงานร่วมกัน</div>
        <div>✅ Claude Code: CLI สั่งงานอัตโนมัติซ้ำๆ</div>
      </div>
      <div class="mt-3 rounded-lg bg-orange-50 p-2 text-[10px]">
        <b class="text-orange-700">Pro ~$20/เดือน (~700 บาท)</b><br>
        <span class="text-gray-600">เหมาะ: Word/Excel/PPT · Co-work · Claude Code</span>
      </div>
    </div>
  </div>

  <div class="rounded-2xl bg-white border border-blue-200 overflow-hidden shadow-sm">
    <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-500"></div>
    <div class="p-4">
      <div class="flex items-center gap-2 mb-2">
        <div class="w-8 h-8 rounded-lg bg-blue-500 text-white flex items-center justify-center font-bold">✦</div>
        <div>
          <div class="font-bold text-blue-800 text-sm">Gemini</div>
          <div class="text-[9px] text-gray-500">Google · Gemini 3 Pro</div>
        </div>
      </div>
      <div class="text-[10px] space-y-1.5 text-gray-700">
        <div>✅ รอบรู้ทุกเรื่อง + ข้อมูลสดใหม่ (Search)</div>
        <div>✅ เชื่อม Google Docs/Sheets/Slides/Gmail</div>
        <div>✅ NotebookLM: สรุปเอกสาร + Podcast เสียง</div>
        <div>✅ Gemini Live: คุยด้วยเสียง/กล้องได้</div>
        <div>✅ รุ่นฟรีใช้เยอะ + โปรโมชั่นการศึกษา</div>
      </div>
      <div class="mt-3 rounded-lg bg-blue-50 p-2 text-[10px]">
        <b class="text-blue-700">ฟรี / Advanced ~$20/เดือน (~700 บาท)</b><br>
        <span class="text-gray-600">เหมาะ: Google Ecosystem · NotebookLM · Live</span>
      </div>
    </div>
  </div>

</div>

<div class="mt-4 rounded-xl bg-gray-50 border border-gray-200 p-3 text-xs text-gray-600 text-center">
  💡 <b>สูตรเลือก:</b> ใช้งานทั่วไป/ภาษาไทย → <b class="text-emerald-600">ChatGPT</b> · Word/Excel/PPT + เอกสารราชการ → <b class="text-orange-600">Claude</b> · ใช้ Google Ecosystem → <b class="text-blue-600">Gemini</b>
</div>

---

# 🧩 ศัพท์ AI 6 คำ ที่ควรรู้ก่อนเริ่ม

<div class="text-sm text-gray-500 mb-4">รู้ไว้ไม่เสียหาย · ใช้ AI ได้เข้าใจขึ้นอีกขั้น</div>

<div class="grid grid-cols-3 gap-3">

  <div class="rounded-2xl bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-200 p-4">
    <div class="flex items-center gap-2 mb-2">
      <div class="text-2xl">🪙</div>
      <div class="font-bold text-blue-800">Token</div>
    </div>
    <div class="text-[11px] text-gray-700 leading-relaxed">
      หน่วยย่อยที่ AI ใช้ "อ่าน–เขียน"<br>
      <span class="text-gray-500">อังกฤษ ~¾ คำ/token · ไทย ~1 ตัวอักษร/token</span>
    </div>
    <div class="mt-2 rounded-lg bg-white/60 p-2 text-[10px] text-blue-700">
      💡 ยิ่ง token มาก → ยิ่งกินค่าใช้จ่าย/เวลา
    </div>
  </div>

  <div class="rounded-2xl bg-gradient-to-br from-purple-50 to-pink-50 border border-purple-200 p-4">
    <div class="flex items-center gap-2 mb-2">
      <div class="text-2xl">🧠</div>
      <div class="font-bold text-purple-800">Context Window</div>
    </div>
    <div class="text-[11px] text-gray-700 leading-relaxed">
      "ความจำสั้น" ของ AI ในแต่ละบทสนทนา<br>
      <span class="text-gray-500">รวม prompt + เอกสารแนบ + คำตอบ</span>
    </div>
    <div class="mt-2 rounded-lg bg-white/60 p-2 text-[10px] text-purple-700">
      💡 คุยนานเกิน → AI ลืมต้น · ขึ้นบทใหม่
    </div>
  </div>

  <div class="rounded-2xl bg-gradient-to-br from-amber-50 to-orange-50 border border-amber-200 p-4">
    <div class="flex items-center gap-2 mb-2">
      <div class="text-2xl">📝</div>
      <div class="font-bold text-amber-800">Prompt</div>
    </div>
    <div class="text-[11px] text-gray-700 leading-relaxed">
      คำสั่ง/คำถามที่เราป้อนให้ AI<br>
      <span class="text-gray-500">ยิ่งชัด + มี context → ยิ่งได้ของดี</span>
    </div>
    <div class="mt-2 rounded-lg bg-white/60 p-2 text-[10px] text-amber-700">
      💡 ดูสูตร R-T-C-F ใน Chapter 4
    </div>
  </div>

  <div class="rounded-2xl bg-gradient-to-br from-rose-50 to-red-50 border border-rose-200 p-4">
    <div class="flex items-center gap-2 mb-2">
      <div class="text-2xl">🌡️</div>
      <div class="font-bold text-rose-800">Temperature</div>
    </div>
    <div class="text-[11px] text-gray-700 leading-relaxed">
      ระดับ "ความสร้างสรรค์" ของคำตอบ<br>
      <span class="text-gray-500">ต่ำ = ตรงเป๊ะ · สูง = ครีเอทีฟ/หลากหลาย</span>
    </div>
    <div class="mt-2 rounded-lg bg-white/60 p-2 text-[10px] text-rose-700">
      💡 งานราชการ → ต่ำ · คำโฆษณา → สูง
    </div>
  </div>

  <div class="rounded-2xl bg-gradient-to-br from-yellow-50 to-amber-50 border border-yellow-300 p-4">
    <div class="flex items-center gap-2 mb-2">
      <div class="text-2xl">⚠️</div>
      <div class="font-bold text-yellow-800">Hallucination</div>
    </div>
    <div class="text-[11px] text-gray-700 leading-relaxed">
      AI "มั่ว" · แต่งข้อมูลที่ดูน่าเชื่อ<br>
      <span class="text-gray-500">มักเกิดกับชื่อคน/เลขระเบียบ/อ้างอิง</span>
    </div>
    <div class="mt-2 rounded-lg bg-white/60 p-2 text-[10px] text-yellow-700">
      💡 ต้องตรวจทานก่อนใช้งานจริงเสมอ
    </div>
  </div>

  <div class="rounded-2xl bg-gradient-to-br from-emerald-50 to-teal-50 border border-emerald-200 p-4">
    <div class="flex items-center gap-2 mb-2">
      <div class="text-2xl">🤖</div>
      <div class="font-bold text-emerald-800">Model</div>
    </div>
    <div class="text-[11px] text-gray-700 leading-relaxed">
      รุ่น/เวอร์ชันของ AI ที่เลือกใช้<br>
      <span class="text-gray-500">GPT-5 · Claude 4.7 · Gemini 3</span>
    </div>
    <div class="mt-2 rounded-lg bg-white/60 p-2 text-[10px] text-emerald-700">
      💡 รุ่นใหม่ = ฉลาดกว่า แต่ช้า/แพงกว่า
    </div>
  </div>

</div>

<div class="mt-4 rounded-xl bg-gradient-to-r from-indigo-50 to-purple-50 border border-indigo-200 p-3 text-xs text-gray-700 text-center">
  📌 <b>สรุปง่ายๆ:</b> <b class="text-blue-600">Token</b> = หน่วยนับ · <b class="text-purple-600">Context</b> = ความจำ · <b class="text-rose-600">Temperature</b> = ความครีเอทีฟ · ที่เหลือรู้ไว้ไม่หลงทาง
</div>

---

# 🎛️ ปรับ 2 ปุ่มสำคัญ — Temperature & Context

<div class="text-sm text-gray-500 mb-4">เลือกให้ถูกกับงาน · ผลลัพธ์เปลี่ยนทันที</div>

<div class="grid grid-cols-2 gap-5">

  <div class="rounded-2xl bg-white border border-rose-200 overflow-hidden shadow-sm">
    <div class="h-1 bg-gradient-to-r from-blue-400 via-amber-400 to-rose-500"></div>
    <div class="p-4">
      <div class="flex items-center gap-2 mb-3">
        <div class="text-2xl">🌡️</div>
        <div>
          <div class="font-bold text-rose-800">Temperature</div>
          <div class="text-[10px] text-gray-500">ความสร้างสรรค์ของคำตอบ · 0.0 – 2.0</div>
        </div>
      </div>
      <div class="space-y-2">
        <div class="rounded-lg bg-blue-50 border border-blue-200 p-2">
          <div class="flex items-center justify-between mb-1">
            <div class="text-[11px] font-bold text-blue-700">🧊 ต่ำ (0.0 – 0.3)</div>
            <div class="text-[9px] text-blue-600 font-mono">เป๊ะ · นิ่ง</div>
          </div>
          <div class="text-[10px] text-gray-700">หนังสือราชการ · แปลเอกสาร · สูตร Excel · สรุปข้อเท็จจริง</div>
        </div>
        <div class="rounded-lg bg-amber-50 border border-amber-200 p-2">
          <div class="flex items-center justify-between mb-1">
            <div class="text-[11px] font-bold text-amber-700">🌤️ กลาง (0.4 – 0.8)</div>
            <div class="text-[9px] text-amber-600 font-mono">สมดุล · ทั่วไป</div>
          </div>
          <div class="text-[10px] text-gray-700">อีเมล · บันทึกข้อความ · สรุปประชุม · ตอบคำถามทั่วไป</div>
        </div>
        <div class="rounded-lg bg-rose-50 border border-rose-200 p-2">
          <div class="flex items-center justify-between mb-1">
            <div class="text-[11px] font-bold text-rose-700">🔥 สูง (0.9 – 1.5)</div>
            <div class="text-[9px] text-rose-600 font-mono">ครีเอทีฟ</div>
          </div>
          <div class="text-[10px] text-gray-700">คำโปรย/สโลแกน · ไอเดียกิจกรรม · บทพูด · โพสต์โซเชียล</div>
        </div>
      </div>
      <div class="mt-3 rounded-lg bg-gray-50 border border-gray-200 p-2 text-[10px] text-gray-600">
        💡 ChatGPT/Claude บน Web ตั้งค่า "กลาง" ให้อัตโนมัติ · ถ้าอยากเปลี่ยน ให้ <b>บอกในคำสั่ง</b> เช่น "ตอบให้เป๊ะที่สุด" หรือ "เสนอไอเดียหลากหลาย"
      </div>
    </div>
  </div>

  <div class="rounded-2xl bg-white border border-purple-200 overflow-hidden shadow-sm">
    <div class="h-1 bg-gradient-to-r from-purple-400 to-pink-500"></div>
    <div class="p-4">
      <div class="flex items-center gap-2 mb-3">
        <div class="text-2xl">🧠</div>
        <div>
          <div class="font-bold text-purple-800">Context Window</div>
          <div class="text-[10px] text-gray-500">"ความจำ" ในแต่ละบทสนทนา · นับเป็น token</div>
        </div>
      </div>
      <div class="space-y-2">
        <div class="rounded-lg bg-purple-50 border border-purple-200 p-2">
          <div class="text-[11px] font-bold text-purple-700 mb-1">📏 รุ่นใหม่ปี 2026 · ใหญ่มาก</div>
          <div class="text-[10px] text-gray-700 space-y-0.5">
            <div>• Claude 4.7 · GPT-5 · Gemini 3 → 200K – 1M tokens</div>
            <div>• เทียบเท่า <b>หนังสือ 500–2,000 หน้า</b> ในครั้งเดียว</div>
          </div>
        </div>
        <div class="rounded-lg bg-pink-50 border border-pink-200 p-2">
          <div class="text-[11px] font-bold text-pink-700 mb-1">⚠️ สัญญาณว่าเต็ม/ใกล้เต็ม</div>
          <div class="text-[10px] text-gray-700 space-y-0.5">
            <div>• AI ตอบช้า · ลืมข้อมูลที่บอกไว้ต้นบท</div>
            <div>• ยกตัวอย่างผิดจากไฟล์ที่แนบมา</div>
            <div>• เริ่มสับสนประเด็น · วนตอบซ้ำ</div>
          </div>
        </div>
        <div class="rounded-lg bg-emerald-50 border border-emerald-200 p-2">
          <div class="text-[11px] font-bold text-emerald-700 mb-1">✅ เคล็ดลับประหยัด context</div>
          <div class="text-[10px] text-gray-700 space-y-0.5">
            <div>• 1 บทสนทนา = 1 งาน → ขึ้นบทใหม่เมื่อเปลี่ยนเรื่อง</div>
            <div>• แนบเฉพาะหน้าที่เกี่ยวข้อง ไม่ต้องยกเล่มมาทั้งหมด</div>
            <div>• สรุปบทสนทนายาว ก่อนถามต่อ</div>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>

---
layout: center
---

# 🎨 ลองเล่นสักนิด...

<div class="text-sm text-gray-500 mb-8">AI อาจฉลาดน้อยกว่าที่คิด... หรือมากกว่าที่คิด?</div>

<div class="grid grid-cols-2 gap-6 max-w-3xl mx-auto">
  <a href="https://quickdraw.withgoogle.com/" target="_blank" class="group">
    <div class="rounded-2xl border-2 border-dashed border-gray-300 hover:border-blue-500 hover:bg-blue-50 p-8 text-center transition-all">
      <div class="text-5xl mb-3">🖍️</div>
      <div class="font-bold text-blue-600 group-hover:text-blue-800">Quick, Draw!</div>
      <div class="text-xs text-gray-500 mt-1">AI ทายภาพวาดของเรา</div>
    </div>
  </a>
  <a href="https://teachablemachine.withgoogle.com/" target="_blank" class="group">
    <div class="rounded-2xl border-2 border-dashed border-gray-300 hover:border-purple-500 hover:bg-purple-50 p-8 text-center transition-all">
      <div class="text-5xl mb-3">🎓</div>
      <div class="font-bold text-purple-600 group-hover:text-purple-800">Teachable Machine</div>
      <div class="text-xs text-gray-500 mt-1">สอน AI ได้ใน 3 นาที</div>
    </div>
  </a>
</div>

---
layout: section
---

# 🎬 Live Demo
## ประยุกต์ใช้ Generative AI กับงานหน้าทัพ
### แก้โจทย์จริง 6 เคส จากงานภาควิชาฯ

<div class="mt-6 text-sm opacity-70">เห็นของจริง · กลับไปใช้ได้จริง</div>

---

# 🔮 Demo 1 · งานสารบรรณ &amp; วิเทศฯ

<div class="text-sm text-gray-500 mb-3">ร่างบันทึก + แปลอีเมลเชิญ Professor ต่างชาติ</div>

<div class="grid grid-cols-2 gap-5">
  <div>
    <div class="rounded-xl bg-blue-50 border border-blue-200 p-3 mb-2 text-xs">
      <span class="font-bold text-blue-700">Step 1 · ขออนุมัติโครงการ</span>
    </div>
    <CopyBox text="ร่างบันทึกข้อความขออนุมัติจัดโครงการสัมมนา 'International AI Seminar 2026' เพื่อยกระดับความเป็นนานาชาติของภาควิชา งบประมาณ 50,000 บาท เรียน หัวหน้าภาควิชา ขอรูปแบบตามระเบียบงานสารบรรณ พ.ศ. 2565">
      <div class="rounded-lg bg-white border border-gray-200 p-3 text-[11px] text-gray-700 leading-relaxed">
        "ร่างบันทึกข้อความ <b>ขออนุมัติจัดโครงการ 'International AI Seminar 2026'</b> เพื่อยกระดับความเป็นนานาชาติของภาควิชา งบ <b>50,000 บาท</b> เรียน <b>คณบดี</b> ขอรูปแบบตามระเบียบงานสารบรรณ 2565"
      </div>
    </CopyBox>
  </div>
  <div>
    <div class="rounded-xl bg-indigo-50 border border-indigo-200 p-3 mb-2 text-xs">
      <span class="font-bold text-indigo-700">Step 2 · เชิญวิทยากร (ต่อเนื่อง)</span>
    </div>
    <CopyBox text="จากโครงการเมื่อกี้ ช่วยร่างอีเมลเชิญ Prof. Hiroshi Tanaka (University of Tokyo) เป็น Keynote Speaker หัวข้อ 'AI for Future Administration' ทางเราออกค่าตั๋วเครื่องบินและที่พัก ขอภาษา Business English โทนสุภาพแต่อบอุ่น">
      <div class="rounded-lg bg-white border border-gray-200 p-3 text-[11px] text-gray-700 leading-relaxed">
        "จากโครงการเมื่อกี้ ร่างอีเมลเชิญ <b>Prof. Hiroshi Tanaka (U. of Tokyo)</b> เป็น Keynote หัวข้อ <b>'AI for Future Administration'</b> ทางเราออกค่าตั๋ว+ที่พัก ขอ <b>Business English</b> โทนอบอุ่น"
      </div>
    </CopyBox>
  </div>
</div>

<div class="mt-3 rounded-xl bg-gradient-to-r from-pink-50 to-orange-50 border border-pink-200 p-2 text-center text-xs text-pink-700">
  💎 <b>จุดว้าว:</b> AI จำ "บริบทตะกี้" ได้ · ไม่ต้องอธิบายโครงการใหม่ซ้ำ
</div>

---

# 🔮 Demo 2 · งานอาคาร &amp; ประกาศภาควิชา

<div class="text-sm text-gray-500 mb-3">ประกาศปิดห้องแล็บ + สร้างคลิป Avatar อ่านประกาศ</div>

<div class="grid grid-cols-2 gap-5">
  <div>
    <div class="rounded-xl bg-amber-50 border border-amber-200 p-3 mb-2 text-xs">
      <span class="font-bold text-amber-700">Step 1 · ร่างประกาศ</span>
    </div>
    <CopyBox text="ร่างประกาศปิดปรับปรุงห้องแล็บคอมฯ ของภาควิชาฯ วันที่ 15-17 พ.ค. 2569 ขอโทนขออภัยในความไม่สะดวก แนะนำห้องแล็บสำรอง พร้อมอีโมจิ 🙏 เพื่อติดบอร์ดประกาศและโพสต์เฟซบุ๊กเพจภาค">
      <div class="rounded-lg bg-white border border-gray-200 p-3 text-[11px] text-gray-700">
        "ร่างประกาศ <b>ปิดปรับปรุงห้องแล็บคอมฯ</b> วันที่ 15-17 พ.ค. 2569 โทนขออภัย แนะนำห้องสำรอง พร้อมอีโมจิ 🙏 — <b>สำหรับติดบอร์ด + โพสต์เพจภาค</b>"
      </div>
    </CopyBox>
    <div class="rounded-xl bg-amber-50 border border-amber-200 p-3 mb-2 mt-2 text-xs">
      <span class="font-bold text-amber-700">Step 2 · แปลงเป็นบทพูด</span>
    </div>
    <CopyBox text="ช่วยแปลงประกาศนี้เป็นบทพูดสำหรับวิดีโอ 30 วินาที ภาษาพูดเป็นกันเองและจริงใจ สำหรับให้ AI Avatar พูด">
      <div class="rounded-lg bg-white border border-gray-200 p-3 text-[11px] text-gray-700">
        "แปลงประกาศนี้เป็นบทพูด <b>30 วินาที</b> · ภาษาพูดเป็นกันเอง สำหรับ <b>AI Avatar</b>"
      </div>
    </CopyBox>
  </div>
  <div class="flex flex-col gap-3">
    <div class="rounded-2xl bg-gradient-to-br from-purple-50 to-pink-50 border border-purple-200 p-4">
      <div class="text-xs font-bold text-purple-700 mb-2 tracking-wider">🎥 TOOLS</div>
      <div class="text-sm space-y-2">
        <div class="flex items-center gap-2"><span class="w-6 h-6 rounded-full bg-purple-200 flex items-center justify-center text-[10px] font-bold">H</span> <b>HeyGen</b> — Avatar พูดไทยได้ดี</div>
        <div class="flex items-center gap-2"><span class="w-6 h-6 rounded-full bg-pink-200 flex items-center justify-center text-[10px] font-bold">D</span> <b>D-ID</b> — Photo → Talking Head</div>
        <div class="flex items-center gap-2"><span class="w-6 h-6 rounded-full bg-orange-200 flex items-center justify-center text-[10px] font-bold">S</span> <b>Synthesia</b> — Avatar มืออาชีพ</div>
      </div>
    </div>
    <div class="rounded-xl bg-gray-50 border border-gray-200 p-3 text-xs text-gray-600 text-center">
      Prompt → Script → Avatar Video <br>
      <b>ใช้เวลา ~10 นาที</b>
    </div>
  </div>
</div>

---

# 🔮 Demo 3 · Chat with PDF (ถามระเบียบ)

<div class="text-sm text-gray-500 mb-3">ไม่ต้องอ่าน 100 หน้า · ถามตรงเลย</div>

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <div class="rounded-xl bg-emerald-50 border border-emerald-200 p-4">
      <div class="text-xs font-bold text-emerald-700 mb-2">📋 โจทย์จริง</div>
      <ul class="text-sm text-gray-700 space-y-2 list-disc pl-5">
        <li>PDF "ระเบียบการเบิกจ่าย" หนา 100 หน้า</li>
        <li>อยากรู้แค่ <b>"ค่าที่พักเบิกได้เท่าไหร่?"</b></li>
        <li>ถ้าเปิดอ่าน → ใช้เวลา 30 นาที</li>
      </ul>
    </div>
    <div class="mt-3 text-sm">
      <b class="text-gray-500 text-xs tracking-wider">⚡ ACTION</b>
      <CopyBox text="ช่วยสรุปเกณฑ์การเบิก 'ค่าเช่าที่พัก' สำหรับพนักงานสายสนับสนุน ว่าเบิกได้คืนละกี่บาท ต้องใช้หลักฐานอะไรบ้าง และอ้างถึงหน้าไหนในเอกสาร">
        <div class="mt-2 rounded-lg bg-white border border-gray-200 p-3 text-[11px] italic">
          "สรุป <b>'ค่าเช่าที่พัก'</b> สำหรับพนักงานสายสนับสนุน เบิกคืนละกี่บาท · ใช้หลักฐานอะไร · อ้างหน้าไหน"
        </div>
      </CopyBox>
    </div>
  </div>
  <div class="flex flex-col items-center justify-center">
    <div class="rounded-2xl bg-gradient-to-br from-emerald-50 to-teal-50 border-2 border-emerald-200 p-6 text-center w-full">
      <div class="text-5xl mb-2">📑</div>
      <div class="text-sm font-bold text-emerald-700">100 หน้า → 1 ประโยค</div>
      <div class="text-xs text-gray-500 mt-2">30 นาที → 10 วินาที</div>
      <div class="mt-4 text-[10px] text-gray-400">
        Best for this: <br>
        <b class="text-gray-600">Claude · Gemini · NotebookLM</b>
      </div>
    </div>
  </div>
</div>

---

# 🔮 Demo 4 · PDF → Infographic

<div class="text-sm text-gray-500 mb-3">เปลี่ยนกำหนดการงานสัมมนา → Infographic สวยใน 5 นาที</div>

<div class="grid grid-cols-4 gap-3 mt-4">
  <div class="rounded-xl bg-gray-50 border border-gray-200 p-4 text-center">
    <div class="text-3xl mb-2">📄</div>
    <div class="text-xs font-bold">1. PDF</div>
    <div class="text-[10px] text-gray-500">กำหนดการ</div>
  </div>
  <div class="rounded-xl bg-blue-50 border border-blue-200 p-4 text-center">
    <div class="text-3xl mb-2">✂️</div>
    <div class="text-xs font-bold text-blue-700">2. Extract</div>
    <div class="text-[10px] text-gray-500">ดึง Text ด้วย AI</div>
  </div>
  <div class="rounded-xl bg-purple-50 border border-purple-200 p-4 text-center">
    <div class="text-3xl mb-2">🎨</div>
    <div class="text-xs font-bold text-purple-700">3. Design</div>
    <div class="text-[10px] text-gray-500">Piktochart/Gamma</div>
  </div>
  <div class="rounded-xl bg-gradient-to-br from-pink-50 to-orange-50 border border-pink-200 p-4 text-center">
    <div class="text-3xl mb-2">🎁</div>
    <div class="text-xs font-bold text-pink-700">4. Share</div>
    <div class="text-[10px] text-gray-500">โพสต์ได้เลย</div>
  </div>
</div>

<CopyBox text="ช่วยดึงข้อความจาก PDF นี้ แล้วสรุปเป็นหัวข้อสั้นๆ (Topic + Bullet Point) สำหรับนำไปทำ Infographic เน้นตัวเลขและกำหนดเวลา">
  <div class="mt-4 rounded-xl bg-gray-50 border border-gray-200 p-3 text-sm text-gray-700 italic">
    <b>Prompt:</b> "ดึงข้อความจาก PDF นี้ สรุปเป็น Topic + Bullet สำหรับ Infographic · เน้นตัวเลขและกำหนดเวลา"
  </div>
</CopyBox>

<div class="mt-3 text-center text-xs text-gray-500">
  🛠️ <b>Tools แนะนำ:</b> Piktochart AI · Gamma · Canva Magic Design · Napkin.ai
</div>

---

# 🔮 Demo 5 · วิเคราะห์ Excel หลายไฟล์

<div class="text-sm text-gray-500 mb-3">เปรียบเทียบราคาวัสดุ 4 เดือน · หาที่ "ขึ้นราคา"</div>

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <div class="rounded-xl bg-red-50 border border-red-200 p-4">
      <div class="text-xs font-bold text-red-700 mb-2">📋 โจทย์จริง</div>
      <ul class="text-sm text-gray-700 space-y-2 list-disc pl-5">
        <li>Excel 4 ไฟล์ (ก.ย.–ธ.ค. 2568)</li>
        <li>หาว่า <b>"รายการไหนปรับราคาขึ้น?"</b> และ <b>"กี่ %?"</b></li>
        <li>เปิดเทียบทีละไฟล์ = ตาลาย</li>
      </ul>
    </div>
    <CopyBox text="ช่วยเปรียบเทียบราคาวัสดุจาก 4 ไฟล์นี้ (M9–M12) สร้างตารางสรุปรายการที่ 'ปรับราคาขึ้น' พร้อมคำนวณ % การเปลี่ยนแปลง เรียงจากมากไปน้อย">
      <div class="mt-3 rounded-lg bg-white border border-gray-200 p-3 text-[11px] italic text-gray-700">
        "เปรียบเทียบ 4 ไฟล์ · ตารางสรุปรายการ <b>'ปรับราคาขึ้น'</b> · คำนวณ <b>%</b> เรียงมาก→น้อย"
      </div>
    </CopyBox>
  </div>
  <div class="rounded-2xl bg-gradient-to-br from-red-50 to-orange-50 border-2 border-red-200 p-5 flex flex-col items-center justify-center">
    <div class="text-5xl mb-3">📈</div>
    <div class="font-bold text-red-700">4 ไฟล์ → 1 ตาราง</div>
    <div class="text-xs text-gray-500 mt-1">ภายใน 30 วินาที</div>
    <div class="mt-4 text-[10px] text-gray-400 text-center">
      <b class="text-gray-600">ChatGPT · Claude</b><br>
      (ทั้งคู่วิเคราะห์ Excel ได้ดี)
    </div>
  </div>
</div>

---

# 🔮 Demo 6 · สร้าง Google Form ฉับไว

<div class="text-sm text-gray-500 mb-3">ให้ AI ร่างคำถาม + เขียนสคริปต์สร้างแบบฟอร์มประเมินงาน ECE Open House อัตโนมัติ</div>

<div class="grid grid-cols-2 gap-5 mt-4">
  <div>
    <div class="rounded-xl bg-orange-50 border border-orange-200 p-3 mb-2 text-xs">
      <span class="font-bold text-orange-700">Step 1 · ร่างคำถาม & ตรวจทาน</span>
    </div>
    <CopyBox text="ช่วยคิดแบบสอบถามประเมินความพึงพอใจ งาน ECE Open House ของภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์ สำหรับนักเรียน ม.ปลาย มีฐานกิจกรรม: แล็บ Computer/Embedded, จำลองฟ้าผ่า, อิเล็กทรอนิกส์, มอเตอร์ ขอคำถาม 5-7 ข้อ (ให้คะแนนฐานต่างๆ และปลายเปิด)">
      <div class="rounded-lg bg-white border border-gray-200 p-3 text-[11px] text-gray-700 leading-relaxed">
        "ร่างคำถามประเมิน <b>ECE Open House</b> ของ <b>ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์</b> มีฐาน <b>แล็บคอม, ฟ้าผ่า, มอเตอร์</b> · คำถาม 5-7 ข้อ <b>ให้คะแนน + ปลายเปิด</b>"
      </div>
    </CopyBox>
    <div class="text-xs text-gray-500 mt-2 ml-1">✓ ผู้ใช้ตรวจสอบคำถาม, ปรับแก้, และกดยืนยัน</div>
  </div>
  <div>
    <div class="rounded-xl bg-amber-50 border border-amber-200 p-3 mb-2 text-xs">
      <span class="font-bold text-amber-700">Step 2 · สั่งเขียนสคริปต์ (Apps Script)</span>
    </div>
    <CopyBox text="โอเค ได้คำถามตามนี้เลย ช่วยเขียน Google Apps Script สำหรับนำไปสร้างเป็น Google Form ให้หน่อย พร้อมอธิบายวิธีนำโค้ดไปรันใน Google Drive แบบทีละขั้นตอน">
      <div class="rounded-lg bg-white border border-gray-200 p-3 text-[11px] text-gray-700 leading-relaxed">
        "โอเค คำถามตามนี้ ช่วยเขียน <b>Google Apps Script</b> สำหรับสร้าง <b>Google Form</b> พร้อม <b>วิธีรันโค้ด</b>"
      </div>
    </CopyBox>
    <div class="flex items-center gap-3 mt-4 p-3 rounded-xl bg-gradient-to-r from-orange-50 to-amber-50 border border-orange-100">
      <span class="text-2xl">⚙️</span>
      <div class="text-xs text-gray-700">
        <strong class="text-sm font-bold text-orange-700 block mb-0.5">ได้ฟอร์มจริงใน 1 นาที</strong>
        ก๊อปปี้โค้ดไปรัน ไม่ต้องนั่งพิมพ์เอง
      </div>
    </div>
  </div>
</div>

<div class="mt-3 rounded-xl bg-gray-50 border border-gray-200 p-2 text-center text-xs text-gray-600">
  💡 <b>หลักการสำคัญ:</b> ทำงานแบบ Human-in-the-loop — ให้เราตรวจคำถามให้ชัวร์ก่อนสั่งเขียนโค้ดเสมอ
</div>

---
layout: center
class: "!px-20"
---

<div class="text-xs tracking-[0.3em] uppercase text-pink-400 mb-4">✨ WOW MOMENT #2</div>

# 🎙️ NotebookLM

<div class="text-lg text-gray-600 mb-6">อัปโหลด PDF ระเบียบพัสดุ 100 หน้า → ได้ <b>Podcast 2 คนคุยภาษาไทย</b> 10 นาที</div>

<div class="grid grid-cols-3 gap-4 max-w-4xl mx-auto">
  <div class="rounded-xl bg-gray-50 p-4 text-center">
    <div class="text-3xl mb-2">📄</div>
    <div class="text-xs font-bold text-gray-700">Upload</div>
    <div class="text-[10px] text-gray-500">PDF/Slides/URL</div>
  </div>
  <div class="rounded-xl bg-indigo-50 p-4 text-center">
    <div class="text-3xl mb-2">⚡</div>
    <div class="text-xs font-bold text-indigo-700">Generate</div>
    <div class="text-[10px] text-gray-500">5 นาที</div>
  </div>
  <div class="rounded-xl bg-gradient-to-br from-pink-50 to-orange-50 border border-pink-200 p-4 text-center">
    <div class="text-3xl mb-2">🎧</div>
    <div class="text-xs font-bold text-pink-700">Podcast</div>
    <div class="text-[10px] text-gray-500">ฟังในรถได้</div>
  </div>
</div>

<div class="mt-6 text-sm text-gray-500 italic">→ Use case: ฟังระเบียบระหว่างขับรถมาทำงาน</div>


---

<div class="text-xs tracking-[0.3em] uppercase text-pink-400 mb-4">✨ WOW MOMENT #3</div>

# 🪄 สร้างสไลด์ด้วย AI (Gamma.app)

<div class="text-lg text-gray-600 mb-8">พิมพ์แค่ "หัวข้อ" → ได้สไลด์ 10 หน้า ดีไซน์สวยหรู พร้อมรูปภาพใน 1 นาที</div>

<div class="grid grid-cols-3 gap-4 max-w-4xl mx-auto flex-1">
  <div class="rounded-2xl bg-white shadow-md p-5 border border-purple-100">
    <div class="text-4xl mb-2">💬</div>
    <div class="text-sm font-bold text-purple-700">พิมพ์แค่ 1 ประโยค</div>
    <div class="text-xs text-gray-500 mt-1">เช่น "แนะนำภาควิชาให้เด็ก ม.ปลาย ฟัง"</div>
  </div>
  <div class="rounded-2xl bg-gradient-to-br from-purple-500 to-indigo-600 text-white shadow-lg p-5">
    <div class="text-4xl mb-2">✨</div>
    <div class="text-sm font-bold">AI จัดโครงร่าง & ค้นรูป</div>
    <div class="text-xs opacity-90 mt-1">เลือกธีม ภาพประกอบ เลย์เอาต์ให้เอง</div>
  </div>
  <div class="rounded-2xl bg-white shadow-md p-5 border border-indigo-100">
    <div class="text-4xl mb-2">📊</div>
    <div class="text-sm font-bold text-indigo-700">พร้อมพรีเซนต์ทันที</div>
    <div class="text-xs text-gray-500 mt-1">Export เป็น PDF หรือ PowerPoint (PPTX) ได้เลย</div>
  </div>
</div>

<div class="mt-8 text-sm text-gray-500 italic">→ Use case: สไลด์รายงานผลด่วน · แนะนำหลักสูตร · นำเสนอโครงการวิจัย</div>

---

# 🧰 เครื่องมือ AI ที่แนะนำ (Cheat Sheet)

<div class="grid grid-cols-3 gap-4 mt-4 text-xs">

  <div class="rounded-xl bg-white border border-gray-200 p-3 shadow-sm">
    <div class="text-[10px] font-bold text-gray-500 tracking-widest mb-2">สไลด์ / PPT</div>
    <ul class="space-y-1.5 text-gray-700">
      <li>⭐ <b>Gamma.app</b> — สวย พิมพ์ประโยคเดียวจบ</li>
      <li>• Beautiful.ai — ดีไซน์เรียบหรูแบบโปร</li>
      <li>• Tome — สาย Storytelling ทำสไลด์เก่ง</li>
    </ul>
  </div>

  <div class="rounded-xl bg-white border border-gray-200 p-3 shadow-sm">
    <div class="text-[10px] font-bold text-gray-500 tracking-widest mb-2">รูปภาพ</div>
    <ul class="space-y-1.5 text-gray-700">
      <li>⭐ <b>DALL·E 3</b> — อยู่ใน ChatGPT คุยง่าย</li>
      <li>• Midjourney — งานศิลป์ คุณภาพสูงสุด</li>
      <li>• Freepik / Leonardo — รูปสวย ใช้งานง่าย</li>
    </ul>
  </div>

  <div class="rounded-xl bg-white border border-gray-200 p-3 shadow-sm">
    <div class="text-[10px] font-bold text-gray-500 tracking-widest mb-2">วิดีโอ / คลิป Avatar</div>
    <ul class="space-y-1.5 text-gray-700">
      <li>⭐ <b>HeyGen</b> — Avatar พูดไทยเนียนมาก</li>
      <li>• Synthesia — Avatar สำหรับองค์กร</li>
      <li>• ElevenLabs — โคลนเสียง (Voice cloning)</li>
    </ul>
  </div>

  <div class="rounded-xl bg-white border border-gray-200 p-3 shadow-sm">
    <div class="text-[10px] font-bold text-gray-500 tracking-widest mb-2">สรุปเอกสาร / วิจัย</div>
    <ul class="space-y-1.5 text-gray-700">
      <li>⭐ <b>NotebookLM</b> — ทำ Podcast จากชีท/PDF</li>
      <li>⭐ <b>Perplexity</b> — ค้นคว้าข้อมูล โชว์แหล่งอ้างอิง</li>
      <li>• SciSpace — เจาะลึกงานวิจัย (Paper)</li>
    </ul>
  </div>

  <div class="rounded-xl bg-white border border-gray-200 p-3 shadow-sm">
    <div class="text-[10px] font-bold text-gray-500 tracking-widest mb-2">Infographic / แผนภาพ</div>
    <ul class="space-y-1.5 text-gray-700">
      <li>⭐ <b>Napkin.ai</b> — เสกแผนภาพจาก Text ทันที</li>
      <li>• Piktochart AI — ช่วยจัดเลย์เอาต์ Infographic</li>
      <li>• Venngage — เทมเพลตสำหรับงานวิชาการเยอะ</li>
    </ul>
  </div>

  <div class="rounded-xl bg-white border border-gray-200 p-3 shadow-sm">
    <div class="text-[10px] font-bold text-gray-500 tracking-widest mb-2">งานสำนักงาน / อีเมล</div>
    <ul class="space-y-1.5 text-gray-700">
      <li>⭐ <b>Claude 3.5</b> — คู่คิดงานเอกสารและสรุปข้อมูล</li>
      <li>⭐ <b>Gemini</b> — เขียนสคริปต์ Google Form/Sheet</li>
      <li>• MS Copilot — ใช้ร่วมกับ Office 365 คล่องตัว</li>
    </ul>
  </div>

</div>

<div class="mt-4 text-center text-[11px] text-gray-600 italic bg-gray-50 rounded-lg p-2 max-w-sm mx-auto">
  ⭐ = เครื่องมือเด่นที่นำมาสาธิตใน Live Demo วันนี้
</div>

---
layout: section
---

# Chapter 3
## Agentic AI
### ยุคของ "AI ที่ทำงานเอง"

<div class="mt-6 text-sm opacity-70">ไม่ใช่แค่ตอบ · แต่ "ลงมือทำ"</div>

---

# 🤖 Agentic AI คืออะไร?

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <div class="rounded-2xl bg-gradient-to-br from-pink-50 to-orange-50 border border-pink-200 p-5">
      <div class="text-xs font-bold text-pink-600 tracking-widest mb-2">DEFINITION</div>
      <p class="text-base text-gray-800 leading-relaxed">
        AI ที่ <b>วางแผนงาน</b> · <b>ใช้เครื่องมือ</b> (เปิดเว็บ, เขียนไฟล์, ส่งเมล) · และ <b>ตัดสินใจเอง</b> เพื่อให้งานสำเร็จ
      </p>
    </div>
    <div class="mt-4 text-sm text-gray-600">
      <b>พูดง่ายๆ:</b> Gen AI เป็น <i>"คนตอบคำถาม"</i><br>
      Agentic AI เป็น <i>"คนรับผิดชอบโปรเจกต์"</i>
    </div>
  </div>

  <div class="space-y-3">
    <div class="flex gap-3 items-start">
      <div class="w-10 h-10 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 text-white flex items-center justify-center font-bold flex-shrink-0">1</div>
      <div>
        <div class="font-bold text-sm">🎯 Planning — วางแผน</div>
        <div class="text-xs text-gray-600">แตกงานใหญ่เป็นขั้นๆ เอง</div>
      </div>
    </div>
    <div class="flex gap-3 items-start">
      <div class="w-10 h-10 rounded-full bg-gradient-to-br from-purple-500 to-pink-600 text-white flex items-center justify-center font-bold flex-shrink-0">2</div>
      <div>
        <div class="font-bold text-sm">🛠️ Tool Use — ใช้เครื่องมือ</div>
        <div class="text-xs text-gray-600">เปิด Chrome, รัน Excel, เขียนโค้ด, ส่งเมล</div>
      </div>
    </div>
    <div class="flex gap-3 items-start">
      <div class="w-10 h-10 rounded-full bg-gradient-to-br from-amber-500 to-orange-600 text-white flex items-center justify-center font-bold flex-shrink-0">3</div>
      <div>
        <div class="font-bold text-sm">🧠 Memory — จดจำบริบท</div>
        <div class="text-xs text-gray-600">รู้ว่าทำอะไรไปแล้ว ต้องทำอะไรต่อ</div>
      </div>
    </div>
    <div class="flex gap-3 items-start">
      <div class="w-10 h-10 rounded-full bg-gradient-to-br from-emerald-500 to-teal-600 text-white flex items-center justify-center font-bold flex-shrink-0">4</div>
      <div>
        <div class="font-bold text-sm">🔄 Self-correction — แก้เอง</div>
        <div class="text-xs text-gray-600">ลองผิดลองถูก จนกว่าจะสำเร็จ</div>
      </div>
    </div>
  </div>
</div>

---

# 🌟 Agentic AI ยุคใหม่ (2026)

<div class="grid grid-cols-2 gap-4 mt-4 text-sm">

  <div class="rounded-2xl bg-white border border-gray-200 p-4 shadow-sm hover:shadow-md transition">
    <div class="flex items-center gap-2 mb-2">
      <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-orange-400 to-red-500 flex items-center justify-center text-lg">🖥️</div>
      <div>
        <div class="font-bold">Claude Computer Use</div>
        <div class="text-[10px] text-gray-500">Anthropic</div>
      </div>
    </div>
    <p class="text-xs text-gray-600">เปิดเว็บไซต์ · คลิก · พิมพ์ · กรอกฟอร์มแทนเราได้จริง</p>
  </div>

  <div class="rounded-2xl bg-white border border-gray-200 p-4 shadow-sm hover:shadow-md transition">
    <div class="flex items-center gap-2 mb-2">
      <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-emerald-400 to-teal-500 flex items-center justify-center text-lg">🤝</div>
      <div>
        <div class="font-bold">ChatGPT Agent / Operator</div>
        <div class="text-[10px] text-gray-500">OpenAI</div>
      </div>
    </div>
    <p class="text-xs text-gray-600">สั่ง "จองตั๋ว/หาข้อมูล/สรุปเว็บ" แล้วเดินไปชงกาแฟได้</p>
  </div>

  <div class="rounded-2xl bg-white border border-gray-200 p-4 shadow-sm hover:shadow-md transition">
    <div class="flex items-center gap-2 mb-2">
      <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-400 to-indigo-500 flex items-center justify-center text-lg">📓</div>
      <div>
        <div class="font-bold">Apple Intelligence (Siri)</div>
        <div class="text-[10px] text-gray-500">Apple</div>
      </div>
    </div>
    <p class="text-xs text-gray-600">เข้าใจบริบทหน้าจอ — สั่ง "ส่งไฟล์นี้ให้หัวหน้าทางเมล" ทำได้ทันที</p>
  </div>

  <div class="rounded-2xl bg-white border border-gray-200 p-4 shadow-sm hover:shadow-md transition">
    <div class="flex items-center gap-2 mb-2">
      <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-purple-400 to-pink-500 flex items-center justify-center text-lg">💼</div>
      <div>
        <div class="font-bold">Copilot / Gemini in Workspace</div>
        <div class="text-[10px] text-gray-500">Microsoft · Google</div>
      </div>
    </div>
    <p class="text-xs text-gray-600">ฝังอยู่ใน Word/Excel/Docs — สั่งงานในโปรแกรมได้เลย</p>
  </div>

</div>

<div class="mt-4 rounded-xl bg-gradient-to-r from-pink-50 to-orange-50 border border-pink-200 p-3 text-center text-xs">
  🔥 <b>Trend สำคัญ:</b> ปี 2026 เจ้าของซอฟต์แวร์ทุกตัว <b>ฝัง Agent เข้าไปในแอป</b> — ไม่ต้องเปิด ChatGPT แยกอีกแล้ว
</div>

---

# 🔬 Agent ทำงานยังไง? (Inside the Loop)

<div class="text-sm text-gray-500 mb-3">โจทย์: "หาตัวอย่างหลักสูตรวิศวกรรม AI จาก 5 มหาวิทยาลัยชั้นนำ สรุปเป็นตาราง"</div>

<div class="space-y-2">

  <div class="flex items-start gap-3 rounded-xl bg-white border border-gray-200 p-3">
    <div class="w-7 h-7 rounded-full bg-blue-500 text-white flex items-center justify-center text-xs font-bold flex-shrink-0">1</div>
    <div class="flex-1 text-sm">
      <b class="text-blue-700">🧠 Think:</b> "ผมต้องค้นหาเว็บไซต์ของ MIT, Stanford, CMU, NTU, จุฬาฯ ก่อน..."
    </div>
  </div>

  <div class="flex items-start gap-3 rounded-xl bg-white border border-gray-200 p-3">
    <div class="w-7 h-7 rounded-full bg-purple-500 text-white flex items-center justify-center text-xs font-bold flex-shrink-0">2</div>
    <div class="flex-1 text-sm">
      <b class="text-purple-700">🛠️ Act:</b> เรียก <code class="bg-purple-50 px-1 rounded text-[11px]">web_search("MIT AI engineering curriculum 2026")</code>
    </div>
  </div>

  <div class="flex items-start gap-3 rounded-xl bg-white border border-gray-200 p-3">
    <div class="w-7 h-7 rounded-full bg-amber-500 text-white flex items-center justify-center text-xs font-bold flex-shrink-0">3</div>
    <div class="flex-1 text-sm">
      <b class="text-amber-700">👀 Observe:</b> อ่านผลลัพธ์ → พบ 10 ลิงก์ → <i>"ลิงก์ที่ 3 คือหลักสูตรจริง ไม่ใช่ข่าว"</i>
    </div>
  </div>

  <div class="flex items-start gap-3 rounded-xl bg-white border border-gray-200 p-3">
    <div class="w-7 h-7 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold flex-shrink-0">4</div>
    <div class="flex-1 text-sm">
      <b class="text-emerald-700">🔁 Repeat:</b> <code class="bg-emerald-50 px-1 rounded text-[11px]">fetch_page(url)</code> → extract → ทำซ้ำกับ 4 มหาลัยที่เหลือ
    </div>
  </div>

  <div class="flex items-start gap-3 rounded-xl bg-gradient-to-r from-pink-50 to-orange-50 border-2 border-pink-300 p-3 shadow-md">
    <div class="w-7 h-7 rounded-full bg-pink-500 text-white flex items-center justify-center text-xs font-bold flex-shrink-0">✓</div>
    <div class="flex-1 text-sm">
      <b class="text-pink-700">📤 Deliver:</b> สร้างตารางเปรียบเทียบ · ส่งกลับให้เรา (รวมเวลา ~3 นาที · เทียบกับคนทำ 3 ชม.)
    </div>
  </div>

</div>

<div class="mt-3 text-center text-xs text-gray-500 italic">
  <b>ReAct Loop:</b> Think → Act → Observe → Repeat · เป็นหัวใจของทุก Agent
</div>

---
layout: center
class: "!px-16"
---

<div class="text-xs tracking-[0.3em] uppercase text-pink-400 mb-2">✨ WOW EXAMPLE</div>

# 🔍 Deep Research

<div class="text-sm text-gray-500 mb-5">สั่งครั้งเดียว · Agent ค้นเว็บ 50+ แหล่ง · ได้รายงานพร้อมอ้างอิง</div>

<div class="grid grid-cols-2 gap-6">
  <div>
    <div class="rounded-2xl bg-gray-900 text-green-300 font-mono text-xs p-4 shadow-lg">
      <div class="text-gray-500 mb-2"># Prompt ของคุณ:</div>
      <div class="text-white leading-relaxed">
        "เขียนรายงาน 10 หน้า <br>
        เปรียบเทียบหลักสูตร AI Engineering <br>
        จาก 5 มหาลัยชั้นนำ ระดับโลก <br>
        พร้อมวิเคราะห์ว่าภาควิชาเรา <br>
        ควรปรับปรุงอะไรบ้าง"
      </div>
    </div>
    <div class="mt-3 text-xs text-gray-500 text-center">⏱️ ใช้เวลา 10–15 นาที</div>
  </div>

  <div class="space-y-2">
    <div class="rounded-lg bg-blue-50 border border-blue-200 p-2 text-xs flex items-center gap-2">
      <span class="text-lg">🌐</span> ค้น Google · Scholar · arXiv <b>(53 แหล่ง)</b>
    </div>
    <div class="rounded-lg bg-purple-50 border border-purple-200 p-2 text-xs flex items-center gap-2">
      <span class="text-lg">📑</span> อ่าน PDF/เว็บ <b>(41 หน้า)</b>
    </div>
    <div class="rounded-lg bg-amber-50 border border-amber-200 p-2 text-xs flex items-center gap-2">
      <span class="text-lg">🧮</span> เปรียบเทียบ · สรุปประเด็น
    </div>
    <div class="rounded-lg bg-emerald-50 border border-emerald-200 p-2 text-xs flex items-center gap-2">
      <span class="text-lg">✍️</span> เขียนรายงาน <b>พร้อม citation</b>
    </div>
    <div class="rounded-lg bg-pink-50 border-2 border-pink-300 p-2 text-xs flex items-center gap-2 font-bold">
      <span class="text-lg">📄</span> ได้รายงาน 10 หน้า · 50+ footnotes
    </div>
  </div>
</div>

<div class="mt-5 rounded-xl bg-gradient-to-r from-pink-50 to-orange-50 border border-pink-200 p-3 text-center text-xs">
  🎯 <b>Tools จริง:</b> ChatGPT Deep Research · Gemini Deep Research · Perplexity Pro · Claude Research
</div>

---

# 🖥️ Computer Use — AI คุม "หน้าจอ" ให้

<div class="text-sm text-gray-500 mb-4">AI เปิดเบราว์เซอร์ คลิก พิมพ์ กรอกฟอร์ม <b>แทนเรา</b></div>

<div class="grid grid-cols-2 gap-6">

  <div>
    <div class="rounded-2xl bg-gradient-to-br from-red-50 to-orange-50 border border-red-200 p-4">
      <div class="text-xs font-bold text-red-700 mb-2 tracking-wider">❌ งานเดิม (30 นาที)</div>
      <ol class="text-sm text-gray-700 space-y-1 list-decimal pl-5">
        <li>เปิดระบบ e-GP / ERP ของมหาลัย</li>
        <li>Login (จำรหัสไม่ค่อยได้)</li>
        <li>กรอกข้อมูลจัดซื้อ 15 ช่อง</li>
        <li>Upload ใบเสนอราคา 3 ไฟล์</li>
        <li>กด "ตรวจสอบ" → เจอ error → แก้</li>
        <li>กดส่ง → รอ Capture หน้าจอยืนยัน</li>
      </ol>
    </div>
  </div>

  <div>
    <div class="rounded-2xl bg-gradient-to-br from-emerald-50 to-teal-50 border-2 border-emerald-300 p-4 shadow-md">
      <div class="text-xs font-bold text-emerald-700 mb-2 tracking-wider">✨ ใช้ Computer Use (3 นาที)</div>
      <div class="rounded-lg bg-white border border-gray-200 p-3 text-xs italic text-gray-700 mb-3">
        "กรอกข้อมูลจัดซื้อตามไฟล์ Excel นี้ ลงระบบ e-GP แล้วแนบใบเสนอราคา 3 ไฟล์ในโฟลเดอร์"
      </div>
      <div class="text-xs text-gray-600 space-y-1">
        <div>🤖 AI เปิด browser</div>
        <div>🤖 Login (ผ่าน SSO ที่เราอนุญาต)</div>
        <div>🤖 กรอก 15 ช่องตาม Excel</div>
        <div>🤖 Upload ไฟล์ · ตรวจสอบ · ส่ง</div>
        <div class="pt-1 font-bold text-emerald-700">👉 เรากดปุ่ม "Approve" ครั้งเดียว</div>
      </div>
    </div>
  </div>

</div>

<div class="mt-4 rounded-xl bg-gray-50 border border-gray-200 p-3 text-center text-xs">
  🛠️ <b>Tools จริง:</b> Claude Computer Use · ChatGPT Operator · Gemini Browser · Manus Agent
</div>

---
layout: center
class: "!px-20"
---

<div class="text-xs tracking-[0.3em] uppercase text-pink-400 mb-2">✨ WOW EXAMPLE</div>

# 🤖🤖🤖 Multi-Agent Team

<div class="text-sm text-gray-500 mb-6">แทนที่จะใช้ AI ตัวเดียว · ให้ <b>"ทีม AI"</b> ทำงานร่วมกัน</div>

<div class="text-sm text-gray-600 mb-4">โจทย์: "จัดงานเปิดบ้านภาควิชา 25 เม.ย. 2569"</div>

<div class="grid grid-cols-4 gap-3 text-xs">
  <div class="rounded-2xl bg-blue-50 border border-blue-200 p-3 text-center">
    <div class="text-3xl mb-2">📋</div>
    <div class="font-bold text-blue-700">Agent-Planner</div>
    <div class="text-[10px] text-gray-600 mt-1">วางกำหนดการ · จัดคิวกิจกรรม</div>
  </div>
  <div class="rounded-2xl bg-purple-50 border border-purple-200 p-3 text-center">
    <div class="text-3xl mb-2">✍️</div>
    <div class="font-bold text-purple-700">Agent-Writer</div>
    <div class="text-[10px] text-gray-600 mt-1">ร่างประกาศ · เชิญ · สคริปต์พิธีกร</div>
  </div>
  <div class="rounded-2xl bg-amber-50 border border-amber-200 p-3 text-center">
    <div class="text-3xl mb-2">🎨</div>
    <div class="font-bold text-amber-700">Agent-Designer</div>
    <div class="text-[10px] text-gray-600 mt-1">ทำโปสเตอร์ · Infographic · Social</div>
  </div>
  <div class="rounded-2xl bg-emerald-50 border border-emerald-200 p-3 text-center">
    <div class="text-3xl mb-2">📊</div>
    <div class="font-bold text-emerald-700">Agent-Analyst</div>
    <div class="text-[10px] text-gray-600 mt-1">สรุปยอดลงทะเบียน · รายงานผล</div>
  </div>
</div>

<div class="mt-5 rounded-2xl bg-gradient-to-r from-pink-50 via-purple-50 to-indigo-50 border border-purple-200 p-4">
  <div class="text-xs font-bold text-purple-700 tracking-wider mb-2">⚡ ORCHESTRATOR (หัวหน้าทีม AI)</div>
  <div class="text-sm text-gray-700">
    สั่งงาน → กระจายให้ Agent ลูกทีม → รวบรวม → <b>ส่งสรุปให้เราอนุมัติ</b> · พอเราบอกว่า "เริ่มได้" → ลงมือทำจริง
  </div>
</div>

<div class="mt-3 text-xs text-center text-gray-500 italic">
  📌 เครื่องมือ: Microsoft Copilot Studio · CrewAI · LangGraph · Claude Sub-agents
</div>

---
layout: section
---

# Chapter 4
## Prompt Engineering
### สั่งงานอย่างไร ให้ได้ดั่งใจ

<div class="mt-6 text-sm opacity-70">AI ไม่ใช่หมอดู · ยิ่งบอกชัด ยิ่งได้ของดี</div>

---

# 🗝️ สูตร R-T-C-F (จำแค่นี้พอ)

<div class="grid grid-cols-4 gap-4 mt-6">
  <div class="rounded-2xl bg-gradient-to-br from-blue-500 to-indigo-600 text-white p-5 relative overflow-hidden">
    <div class="absolute -top-4 -right-4 text-6xl opacity-20">R</div>
    <div class="relative z-10">
      <div class="text-2xl mb-2">🎭</div>
      <div class="font-bold mb-1">Role</div>
      <div class="text-xs opacity-90">"รับบทเป็น เจ้าหน้าที่ภาควิชา..."</div>
    </div>
  </div>
  <div class="rounded-2xl bg-gradient-to-br from-purple-500 to-pink-600 text-white p-5 relative overflow-hidden">
    <div class="absolute -top-4 -right-4 text-6xl opacity-20">T</div>
    <div class="relative z-10">
      <div class="text-2xl mb-2">📝</div>
      <div class="font-bold mb-1">Task</div>
      <div class="text-xs opacity-90">"ร่างบันทึกขออนุมัติจัดโครงการ..."</div>
    </div>
  </div>
  <div class="rounded-2xl bg-gradient-to-br from-amber-500 to-orange-600 text-white p-5 relative overflow-hidden">
    <div class="absolute -top-4 -right-4 text-6xl opacity-20">C</div>
    <div class="relative z-10">
      <div class="text-2xl mb-2">🧩</div>
      <div class="font-bold mb-1">Context</div>
      <div class="text-xs opacity-90">"งบ 50,000 บาท · เรียนคณบดี..."</div>
    </div>
  </div>
  <div class="rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 text-white p-5 relative overflow-hidden">
    <div class="absolute -top-4 -right-4 text-6xl opacity-20">F</div>
    <div class="relative z-10">
      <div class="text-2xl mb-2">📦</div>
      <div class="font-bold mb-1">Format</div>
      <div class="text-xs opacity-90">"รูปแบบบันทึกราชการ · 1 หน้า"</div>
    </div>
  </div>
</div>

<div class="mt-8 rounded-2xl bg-gray-50 border border-gray-200 p-5">
  <div class="text-xs text-gray-500 mb-2 tracking-wider">ตัวอย่างเต็มรูปแบบ</div>
  <div class="text-sm text-gray-800 leading-relaxed">
    <span class="bg-blue-100 text-blue-800 px-1 rounded">รับบทเป็นเจ้าหน้าที่บริหารงานทั่วไปของภาควิชาวิศวกรรมคอมพิวเตอร์</span>
    <span class="bg-purple-100 text-purple-800 px-1 rounded">ช่วยร่างบันทึกข้อความขออนุมัติจัดโครงการอบรม</span>
    <span class="bg-amber-100 text-amber-800 px-1 rounded">"AI for Everyone" งบประมาณ 30,000 บาท เรียน หัวหน้าภาควิชา</span>
    <span class="bg-emerald-100 text-emerald-800 px-1 rounded">ขอรูปแบบตามระเบียบงานสารบรรณ 2565 ความยาว 1 หน้า A4</span>
  </div>
</div>

---

# ⚡ Specific vs General — ต่างกันชัด

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="rounded-2xl bg-red-50 border border-red-200 p-5 opacity-80">
    <div class="flex items-center gap-2 mb-2">
      <div class="w-6 h-6 rounded-full bg-red-500 text-white flex items-center justify-center text-xs font-bold">✗</div>
      <div class="text-xs font-bold text-red-700 tracking-wider">GENERAL</div>
    </div>
    <div class="text-base text-gray-800">"เขียนอีเมลลางานให้หน่อย"</div>
    <div class="mt-4 text-xs text-gray-500 italic">→ ได้แบบกลางๆ · อาจไม่ตรงจริตเรา · ต้องแก้เยอะ</div>
  </div>
  <div class="rounded-2xl bg-gradient-to-br from-emerald-50 to-teal-50 border-2 border-emerald-300 p-5 shadow-md">
    <div class="flex items-center gap-2 mb-2">
      <div class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold">✓</div>
      <div class="text-xs font-bold text-emerald-700 tracking-wider">SPECIFIC</div>
    </div>
    <CopyBox text="เขียนอีเมลลางาน เนื่องจากป่วยเป็นไข้หวัดใหญ่ ขอลา 2 วัน (27-28 ม.ค.) ส่งถึงหัวหน้าภาควิชา ขอภาษาสุภาพและเป็นทางการ ความยาวไม่เกิน 4 บรรทัด">
      <div class="text-sm text-gray-800">
        "เขียนอีเมลลางาน <b>เนื่องจากป่วยเป็นไข้หวัดใหญ่</b><br>
        ขอลา <b>2 วัน (27-28 ม.ค.)</b><br>
        ส่งถึง <b>หัวหน้าภาควิชา</b><br>
        ขอภาษา <b>สุภาพและเป็นทางการ</b> · ไม่เกิน 4 บรรทัด"
      </div>
    </CopyBox>
    <div class="mt-3 text-xs text-emerald-600 font-semibold">→ ได้ผลลัพธ์พร้อมใช้ ไม่ต้องแก้</div>
  </div>
</div>

---

# 🔁 ไม่ถูกใจ? คุยต่อได้ ไม่ต้องเริ่มใหม่

<div class="text-sm text-gray-500 mb-4">AI คือ "แชท" · สั่งแก้ได้เรื่อยๆ จนกว่าจะใช่</div>

<div class="space-y-3 max-w-3xl mx-auto">
  <div class="flex justify-end">
    <div class="bg-blue-500 text-white px-4 py-2 rounded-2xl rounded-br-sm text-sm max-w-md shadow">
      "ร่างหนังสือเชิญวิทยากรให้หน่อย"
    </div>
  </div>
  <div class="flex justify-start">
    <div class="bg-gray-100 px-4 py-2 rounded-2xl rounded-bl-sm text-sm max-w-md italic text-gray-600">
      🤖 (ร่างมาให้... ยาวไปและดูโบราณ)
    </div>
  </div>
  <div class="flex justify-end">
    <div class="bg-blue-500 text-white px-4 py-2 rounded-2xl rounded-br-sm text-sm max-w-md shadow">
      "สั้นลงครึ่งนึง ปรับภาษาให้ทันสมัย เลิกใช้คำฟุ่มเฟือย"
    </div>
  </div>
  <div class="flex justify-start">
    <div class="bg-gray-100 px-4 py-2 rounded-2xl rounded-bl-sm text-sm max-w-md italic text-gray-600">
      🤖 (ปรับให้ใหม่...)
    </div>
  </div>
  <div class="flex justify-end">
    <div class="bg-blue-500 text-white px-4 py-2 rounded-2xl rounded-br-sm text-sm max-w-md shadow">
      "เก็บโครงนี้ไว้ แต่เพิ่มความอบอุ่นใส่ลงไปนิด"
    </div>
  </div>
</div>

<div class="mt-6 text-center text-xs text-gray-500">
  💡 <b>สูตรลัด:</b> "สั้นลง" · "เป็นทางการกว่านี้" · "ใส่ Emoji" · "เปลี่ยนโทนให้อบอุ่น" · "ขอเป็นตาราง"
</div>

---

# 🪄 AI เสกสูตร Excel (ลืมจำสูตรได้เลย)

<div class="grid grid-cols-2 gap-4 mt-4 text-sm">

  <div class="rounded-2xl bg-white border border-emerald-200 p-4">
    <div class="text-xs font-bold text-emerald-700 mb-1">1. แยกชื่อ-นามสกุล</div>
    <div class="text-[11px] text-gray-500 mb-2">"นายสมชาย ใจดี" → 2 ช่อง</div>
    <div class="rounded-lg bg-emerald-50 p-2 text-[11px] italic text-gray-700">
      "เขียนสูตร Excel แยกคำหน้าและคำหลังจาก A2 โดยใช้ช่องว่างเป็นตัวแบ่ง"
    </div>
  </div>

  <div class="rounded-2xl bg-white border border-blue-200 p-4">
    <div class="text-xs font-bold text-blue-700 mb-1">2. ตัดเกรด (Nested IF)</div>
    <div class="text-[11px] text-gray-500 mb-2">80↑=A, 70↑=B, 60↑=C</div>
    <div class="rounded-lg bg-blue-50 p-2 text-[11px] italic text-gray-700">
      "เขียนสูตรตัดเกรดจาก A2: ≥80=A, ≥70=B, ≥60=C, นอกนั้น F"
    </div>
  </div>

  <div class="rounded-2xl bg-white border border-purple-200 p-4">
    <div class="text-xs font-bold text-purple-700 mb-1">3. VLOOKUP ข้าม Sheet</div>
    <div class="text-[11px] text-gray-500 mb-2">ดึงราคาจาก PriceList</div>
    <div class="rounded-lg bg-purple-50 p-2 text-[11px] italic text-gray-700">
      "เขียน VLOOKUP ดึงราคาจาก Sheet 'PriceList' โดยอ้างรหัสสินค้าใน A2"
    </div>
  </div>

  <div class="rounded-2xl bg-white border border-pink-200 p-4">
    <div class="text-xs font-bold text-pink-700 mb-1">4. คำนวณอายุงาน</div>
    <div class="text-[11px] text-gray-500 mb-2">จากวันที่เริ่มถึงวันนี้</div>
    <div class="rounded-lg bg-pink-50 p-2 text-[11px] italic text-gray-700">
      "คำนวณอายุงานจาก A2 ถึงวันนี้ ผลเป็น 'X ปี Y เดือน'"
    </div>
  </div>

</div>

<div class="mt-4 rounded-xl bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200 p-3 text-xs text-center text-gray-700">
  💎 <b>Pro tip:</b> Upload ไฟล์ Excel จริงให้ AI ดูก่อน → มันจะเขียนสูตรที่ตรงกับข้อมูลเราเป๊ะ
</div>

---

# 🎯 Analogy — อธิบายเรื่องยากให้ "เห็นภาพ"

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <div class="rounded-2xl bg-gradient-to-br from-purple-50 to-pink-50 border border-purple-200 p-5">
      <div class="text-xs font-bold text-purple-700 tracking-wider mb-2">PROMPT TEMPLATE</div>
      <CopyBox text="ช่วยอธิบาย [หัวข้อยาก] ให้เข้าใจง่าย โดยเปรียบเทียบกับ [เรื่องในชีวิตประจำวัน]">
        <div class="text-sm font-mono text-gray-700 bg-white rounded-lg p-3 border">
          "ช่วยอธิบาย <b class="text-purple-600">[หัวข้อยาก]</b><br>
          โดยเปรียบเทียบกับ<br>
          <b class="text-pink-600">[เรื่องในชีวิตประจำวัน]</b>"
        </div>
      </CopyBox>
    </div>
  </div>
  <div class="space-y-3">
    <div class="rounded-xl bg-white border border-gray-200 p-3 shadow-sm">
      <div class="text-xs font-bold text-gray-500 mb-1">ตัวอย่าง 1</div>
      <div class="text-sm">"อธิบาย <b>Blockchain</b> เหมือน<br><b class="text-purple-600">ป้าข้างบ้านที่จำหนี้ได้แม่น</b>"</div>
    </div>
    <div class="rounded-xl bg-white border border-gray-200 p-3 shadow-sm">
      <div class="text-xs font-bold text-gray-500 mb-1">ตัวอย่าง 2</div>
      <div class="text-sm">"อธิบาย <b>ระบบ ERP</b> เหมือน<br><b class="text-purple-600">ตู้เย็นในบ้านที่รู้ว่ามีอะไรเหลือ</b>"</div>
    </div>
    <div class="rounded-xl bg-white border border-gray-200 p-3 shadow-sm">
      <div class="text-xs font-bold text-gray-500 mb-1">ตัวอย่าง 3</div>
      <div class="text-sm">"อธิบาย <b>Cloud</b> เหมือน<br><b class="text-purple-600">ตู้เซฟธนาคารที่ฝาก-ถอนได้ตลอด</b>"</div>
    </div>
  </div>
</div>

---

# 😌 ปรับโทนเสียง — จาก "โกรธ" เป็น "มืออาชีพ"

<div class="text-sm text-gray-500 mb-4">เหมาะสุดสำหรับตอบ complaint · ทวงงาน · แจ้งเรื่องยากๆ</div>

<div class="grid grid-cols-2 gap-6">
  <div class="rounded-2xl bg-red-50 border border-red-200 p-5">
    <div class="text-xs font-bold text-red-700 tracking-wider mb-2">🤬 BEFORE</div>
    <p class="text-sm text-gray-800 italic leading-relaxed">"ทำไมยังไม่ส่งของ?! รอมา 2 อาทิตย์แล้ว ถ้าทำไม่ได้ก็บอกเลิกสัญญาไปเลย!"</p>
  </div>
  <div class="rounded-2xl bg-gradient-to-br from-blue-50 to-indigo-50 border-2 border-blue-300 p-5 shadow-md">
    <div class="text-xs font-bold text-blue-700 tracking-wider mb-2">👔 AFTER (AI ช่วยเกลา)</div>
    <p class="text-sm text-gray-800 leading-relaxed">"ขออนุญาตสอบถามสถานะการจัดส่งครับ เนื่องจากทางภาควิชาจำเป็นต้องใช้ในการเรียนการสอน หากติดขัดตรงไหนแจ้งได้เลย ยินดีช่วยประสานงานครับ"</p>
  </div>
</div>

<CopyBox text="ช่วยปรับข้อความนี้ให้สุภาพ เป็นมืออาชีพ และมี Empathy (เห็นอกเห็นใจ) โดยคงเจตนาเดิมไว้">
  <div class="mt-5 rounded-xl bg-gray-50 border border-gray-200 p-3 text-center text-sm text-gray-700">
    <b class="text-gray-500">Prompt:</b> "ช่วยปรับข้อความนี้ให้ <b>สุภาพ · เป็นมืออาชีพ · มี Empathy</b> โดยคงเจตนาเดิม"
  </div>
</CopyBox>

---

# 🔎 ต้องการข้อมูลจริง? ใช้ Perplexity

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <div class="text-sm font-bold text-gray-700 mb-2">ทำไม ChatGPT ไม่พอ?</div>
    <ul class="text-sm text-gray-600 space-y-2 list-disc pl-5">
      <li>Gen AI "มั่วได้" (Hallucination) ถ้าไม่มีข้อมูล</li>
      <li>ข้อมูลอาจเก่า · ไม่ Real-time</li>
      <li>ไม่มี "แหล่งอ้างอิง" ให้ตรวจ</li>
    </ul>
    <div class="mt-4 rounded-2xl bg-gradient-to-br from-teal-50 to-cyan-50 border border-teal-200 p-4">
      <div class="text-xs font-bold text-teal-700 tracking-wider mb-1">✅ SOLUTION</div>
      <div class="font-bold text-teal-800">Perplexity.ai</div>
      <p class="text-xs text-gray-700 mt-1">Google Search + AI Summary + <b>Citation ทุกประโยค</b> ✨</p>
    </div>
  </div>
  <div class="flex items-center justify-center">
    <div class="text-center">
      <div class="text-7xl">🔎</div>
      <div class="mt-3 text-sm text-gray-500 italic">"Trust, but Verify"</div>
      <div class="mt-1 text-xs text-gray-400">เชื่อได้ · แต่ต้องตรวจเสมอ</div>
    </div>
  </div>
</div>

---

# 🛡️ ข้อควรระวัง 3 ข้อ

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="rounded-2xl bg-white border-t-4 border-red-500 shadow-sm p-5 text-center">
    <div class="text-4xl mb-3">🔒</div>
    <h3 class="font-bold text-red-700 mb-2">ห้ามใส่ความลับ</h3>
    <p class="text-xs text-gray-600">รหัสผ่าน · เงินเดือน · ข้อมูลส่วนตัวนิสิต/อาจารย์ · เลขบัตร ปชช.</p>
    <div class="text-[10px] text-gray-400 mt-2 italic">(ถือว่า upload ขึ้น server เขา)</div>
  </div>
  <div class="rounded-2xl bg-white border-t-4 border-amber-500 shadow-sm p-5 text-center">
    <div class="text-4xl mb-3">🧐</div>
    <h3 class="font-bold text-amber-700 mb-2">ตรวจก่อนส่ง</h3>
    <p class="text-xs text-gray-600">AI มั่วได้ (Hallucination) โดยเฉพาะตัวเลข · วันที่ · ชื่อคน</p>
    <div class="text-[10px] text-gray-400 mt-2 italic">"AI ฉลาด — แต่เราต้องฉลาดกว่า"</div>
  </div>
  <div class="rounded-2xl bg-white border-t-4 border-emerald-500 shadow-sm p-5 text-center">
    <div class="text-4xl mb-3">⚖️</div>
    <h3 class="font-bold text-emerald-700 mb-2">ลิขสิทธิ์</h3>
    <p class="text-xs text-gray-600">ภาพจาก AI ปัจจุบันยังจดลิขสิทธิ์ไม่ได้ (Public Domain)</p>
    <div class="text-[10px] text-gray-400 mt-2 italic">ใช้ได้ · แต่คนอื่นใช้ได้เหมือนกัน</div>
  </div>
</div>

---
layout: center
class: "text-center"
---

# 🛠️ Engineering AI Prompter
## Web App รวมสูตรสำเร็จ สำหรับชาวภาควิชา

<div class="mt-6 rounded-3xl bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-600 text-white p-8 max-w-4xl mx-auto shadow-2xl flex items-center gap-8">
  <div class="flex-1 text-left">
    <div class="text-[10px] tracking-widest opacity-70 mb-2">EXCLUSIVE · FREE</div>
    <h3 class="text-2xl font-bold mb-3">16 สถานการณ์ พร้อมใช้งาน</h3>
    <p class="text-sm opacity-90 mb-4 leading-relaxed">
      ธุรการ · พัสดุ · อาคาร · ศูนย์คอม · วิจัย — ครบทุกงาน<br>
      <b>เลือก → เติมคำ → Copy → ใช้ได้เลย</b>
    </p>
    <a href="https://script.google.com/macros/s/AKfycbyF-DEUCV60wUqzKYLwLmFvoUC-PUhDPsPpwygDC4H1XscyYz66kWwhGwcliqNhk5CY/exec" target="_blank" class="inline-block text-sm bg-white text-indigo-700 px-4 py-2 rounded-lg font-bold hover:bg-yellow-200 transition">
      🔗 เปิด Web App
    </a>
  </div>
  <div class="bg-white p-3 rounded-2xl flex-shrink-0 shadow-lg">
    <img src="/qrcode_webapp.png" class="w-36 h-36" />
    <div class="text-[9px] text-gray-500 text-center mt-1">สแกนเลย</div>
  </div>
</div>

---
layout: cover
background: https://images.unsplash.com/photo-1509042239860-f550ce710b93?q=80&w=1920
---

# พักเบรก ☕ 15 นาที

## 10:30 – 10:45 น.

<div class="mt-6 text-sm opacity-80 italic">กลับมาลุย Workshop ต่อครับ!</div>

---
layout: section
---

# Part 2
## Super Support Workshop
### Workshop · ลงมือทำกับงานจริงของตัวเอง

<div class="mt-6 text-sm opacity-70">10:45 – 12:00 น. · ลงมือประยุกต์ใช้จริง</div>

---

# 🚀 ขั้นตอนการทำงาน (ง่ายๆ 4 ขั้น)

<div class="grid grid-cols-4 gap-4 mt-6">
  <div class="rounded-2xl bg-white border border-blue-200 p-4 relative">
    <div class="absolute -top-3 -left-3 w-8 h-8 rounded-full bg-blue-500 text-white flex items-center justify-center font-bold shadow-md">1</div>
    <div class="mt-2 text-sm font-bold text-blue-800">เลือกงาน</div>
    <div class="text-xs text-gray-600 mt-1">นำงานจริงของตัวเองมาตั้งโจทย์</div>
  </div>
  <div class="rounded-2xl bg-white border border-purple-200 p-4 relative">
    <div class="absolute -top-3 -left-3 w-8 h-8 rounded-full bg-purple-500 text-white flex items-center justify-center font-bold shadow-md">2</div>
    <div class="mt-2 text-sm font-bold text-purple-800">ระบุปัญหา</div>
    <div class="text-xs text-gray-600 mt-1">หางานที่ซ้ำซ้อนหรือใช้เวลานาน</div>
  </div>
  <div class="rounded-2xl bg-white border border-amber-200 p-4 relative">
    <div class="absolute -top-3 -left-3 w-8 h-8 rounded-full bg-amber-500 text-white flex items-center justify-center font-bold shadow-md">3</div>
    <div class="mt-2 text-sm font-bold text-amber-800">สร้าง Prompt</div>
    <div class="text-xs text-gray-600 mt-1">ปรับใช้สูตร R-T-C-F</div>
  </div>
  <div class="rounded-2xl bg-white border border-emerald-200 p-4 relative">
    <div class="absolute -top-3 -left-3 w-8 h-8 rounded-full bg-emerald-500 text-white flex items-center justify-center font-bold shadow-md">4</div>
    <div class="mt-2 text-sm font-bold text-emerald-800">ส่งผลงาน</div>
    <div class="text-xs text-gray-600 mt-1">แชร์ Prompt และผลลัพธ์ในกลุ่ม</div>
  </div>
</div>



---

# 🏆 โจทย์ตัวอย่าง 6 ภารกิจ

<div class="grid grid-cols-3 gap-3 mt-4 text-xs">
  <div class="rounded-xl bg-blue-50 border border-blue-200 p-3">
    <div class="flex items-center gap-1 mb-1">
      <span class="w-5 h-5 rounded-full bg-blue-500 text-white flex items-center justify-center text-[10px] font-bold">1</span>
      <b class="text-blue-700">ธุรการภาค</b>
    </div>
    <div class="text-gray-700">ร่างบันทึกเชิญ กรรมการสอบวิทยานิพนธ์ 3 คน พร้อมตารางนัดหมาย</div>
  </div>
  <div class="rounded-xl bg-amber-50 border border-amber-200 p-3">
    <div class="flex items-center gap-1 mb-1">
      <span class="w-5 h-5 rounded-full bg-amber-500 text-white flex items-center justify-center text-[10px] font-bold">2</span>
      <b class="text-amber-700">อาคาร/ครุภัณฑ์</b>
    </div>
    <div class="text-gray-700">ประกาศ "ย้ายห้องแล็บชั่วคราว" ให้นิสิตไม่งง + ทำอินโฟกราฟิก</div>
  </div>
  <div class="rounded-xl bg-emerald-50 border border-emerald-200 p-3">
    <div class="flex items-center gap-1 mb-1">
      <span class="w-5 h-5 rounded-full bg-emerald-500 text-white flex items-center justify-center text-[10px] font-bold">3</span>
      <b class="text-emerald-700">พัสดุ/จัดซื้อ</b>
    </div>
    <div class="text-gray-700">เปรียบเทียบสเปกคอมพิวเตอร์ 2 รุ่น สรุปให้กรรมการตรวจรับ</div>
  </div>
  <div class="rounded-xl bg-purple-50 border border-purple-200 p-3">
    <div class="flex items-center gap-1 mb-1">
      <span class="w-5 h-5 rounded-full bg-purple-500 text-white flex items-center justify-center text-[10px] font-bold">4</span>
      <b class="text-purple-700">บริการการศึกษา</b>
    </div>
    <div class="text-gray-700">ร่าง Q&amp;A ตอบนิสิต "ลงทะเบียนเรียนซ้ำ / ขอใบรับรอง"</div>
  </div>
  <div class="rounded-xl bg-pink-50 border border-pink-200 p-3">
    <div class="flex items-center gap-1 mb-1">
      <span class="w-5 h-5 rounded-full bg-pink-500 text-white flex items-center justify-center text-[10px] font-bold">5</span>
      <b class="text-pink-700">PR ภาควิชา</b>
    </div>
    <div class="text-gray-700">คิด Caption + แคปชัน 3 โพสต์ โปรโมต "งานเปิดบ้านภาควิชา"</div>
  </div>
  <div class="rounded-xl bg-teal-50 border border-teal-200 p-3">
    <div class="flex items-center gap-1 mb-1">
      <span class="w-5 h-5 rounded-full bg-teal-500 text-white flex items-center justify-center text-[10px] font-bold">6</span>
      <b class="text-teal-700">งานวิจัย/แผน</b>
    </div>
    <div class="text-gray-700">สรุปโครงการวิจัยย้อนหลัง 3 ปี เป็นตารางเสนอ หน.ภาค</div>
  </div>
</div>

<div class="mt-5 text-center">
  <div class="inline-block rounded-full bg-gradient-to-r from-pink-500 to-orange-500 text-white px-5 py-2 text-sm font-bold shadow-lg animate-pulse">
    ไม่มีผิด · ไม่มีถูก · ลองเล่นให้เต็มที่!
  </div>
</div>

---
layout: center
class: "text-center"
---

# 🎤 Show &amp; Tell
### โชว์ผลงาน · แลกเปลี่ยนไอเดีย

<div class="mt-6 text-sm text-gray-500">แชร์ไอเดีย Prompt สุดเจ๋งเพื่อนำไปปรับใช้ 🎁</div>

<div class="mt-8 grid grid-cols-3 gap-4 max-w-3xl mx-auto">
  <div class="rounded-2xl bg-gradient-to-br from-yellow-100 to-amber-200 p-4 text-center">
    <div class="text-4xl mb-1">🥇</div>
    <div class="text-xs font-bold text-amber-800">Most Practical</div>
  </div>
  <div class="rounded-2xl bg-gradient-to-br from-pink-100 to-rose-200 p-4 text-center">
    <div class="text-4xl mb-1">🎨</div>
    <div class="text-xs font-bold text-pink-800">Most Creative</div>
  </div>
  <div class="rounded-2xl bg-gradient-to-br from-blue-100 to-indigo-200 p-4 text-center">
    <div class="text-4xl mb-1">🏆</div>
    <div class="text-xs font-bold text-blue-800">Prompt of the Day</div>
  </div>
</div>

---
layout: center
class: "text-center"
---

# 🎯 Key Takeaways

<div class="grid grid-cols-2 gap-5 mt-8 max-w-4xl mx-auto text-left">
  <div class="rounded-2xl bg-white border border-indigo-100 p-5 shadow-sm">
    <div class="text-3xl mb-2">1️⃣</div>
    <div class="font-bold text-indigo-800">รู้ 3 ยุคของ AI</div>
    <div class="text-sm text-gray-600 mt-1">Chat → Gen → Agentic · แต่ละยุคมีของเล่นต่างกัน</div>
  </div>
  <div class="rounded-2xl bg-white border border-purple-100 p-5 shadow-sm">
    <div class="text-3xl mb-2">2️⃣</div>
    <div class="font-bold text-purple-800">เลือกเครื่องมือถูก</div>
    <div class="text-sm text-gray-600 mt-1">ไทย/วิเคราะห์ = Claude · รอบด้าน = ChatGPT · Google = Gemini</div>
  </div>
  <div class="rounded-2xl bg-white border border-amber-100 p-5 shadow-sm">
    <div class="text-3xl mb-2">3️⃣</div>
    <div class="font-bold text-amber-800">สูตร R-T-C-F</div>
    <div class="text-sm text-gray-600 mt-1">Role · Task · Context · Format — จำไว้สั่งไม่ผิด</div>
  </div>
  <div class="rounded-2xl bg-white border border-emerald-100 p-5 shadow-sm">
    <div class="text-3xl mb-2">4️⃣</div>
    <div class="font-bold text-emerald-800">ใช้บ่อย = เก่งเอง</div>
    <div class="text-sm text-gray-600 mt-1">เริ่มจาก 1 งาน/วัน · 1 เดือนจะติดเป็นนิสัย</div>
  </div>
</div>

---
layout: cover
background: https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=1920
---

# ขอบคุณครับ

## Q & A

<div class="mt-8 inline-block rounded-2xl bg-white/10 backdrop-blur-md border border-white/20 p-5 text-left">
  <div class="text-sm opacity-80">ติดต่อเพิ่มเติม</div>
  <div class="text-base mt-1">📧 ruslee.s@eng.kmutnb.ac.th</div>
  <div class="text-xs opacity-60 mt-3 italic">สไลด์นี้ช่วยสร้างด้วย AI (Slidev + Claude + Gemini) 🤖</div>
</div>
