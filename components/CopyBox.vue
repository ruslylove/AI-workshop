<script setup>
import { ref } from 'vue'

const props = defineProps({
  text: {
    type: String,
    required: true
  }
})

const copied = ref(false)

const handleCopy = async () => {
  try {
    await navigator.clipboard.writeText(props.text)
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}
</script>

<template>
  <div 
    class="relative group cursor-pointer transition-all duration-200 hover:scale-[1.01]" 
    @click="handleCopy"
  >
    <slot />
    
    <div class="absolute top-2 right-2 transition-opacity duration-200" :class="copied ? 'opacity-100' : 'opacity-0 group-hover:opacity-100'">
         <div v-if="copied" class="flex items-center gap-1 bg-green-500 text-white px-2 py-1 rounded text-[10px] font-bold shadow-md animate-bounce">
            ✓ Copied!
         </div>
         <div v-else class="flex items-center gap-1 bg-white/90 text-gray-500 px-2 py-1 rounded text-[10px] shadow border border-gray-200">
            📋 Click to Copy
         </div>
    </div>
  </div>
</template>
