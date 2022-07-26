<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import { addTorrent } from '@/helpers/api'

let model: Ref<File | null> = ref(null);

function upload() {
  let file = model.value;
  if (file !== null) {
    addTorrent(file);
  } else {
    console.log("Select file before upload");
  }
}

</script>

<template>
  <q-file filled bottom-slots v-model="model" label="Label" counter>
    <template v-slot:prepend>
      <q-btn icon="cloud_upload" @click="upload" />
    </template>
    <template v-slot:append>
      <q-icon name="close" @click.stop.prevent="model = null" class="cursor-pointer" />
    </template>

    <template v-slot:hint>
      Choose Torrent
    </template>
  </q-file>
</template>