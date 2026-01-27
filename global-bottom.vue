<template>
  <footer
    v-if="$nav.currentLayout !== 'cover'"
    class="absolute bottom-1 right-2 p-1 text-xs text-gray-400 z-50"
  >
    <SlideCurrentNo />
  </footer>
</template>
