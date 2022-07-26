<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import { Buffer } from 'buffer'
import { deleteTorrent } from '@/helpers/api'
import { prettySize } from "@/helpers/pretty"

const confirm = ref(false);

const props = defineProps<{
  id: number,
  name: string,
  totalSize: number,
  progress: number,
  rateDownload: number,
  rateUpload: number,
}>()

function deleteAction() {
  deleteTorrent([props.id]);
}

</script>

<template>
  <q-item>
    <q-item-section>
      <q-item-label>{{ name }}</q-item-label>
      <q-item-label caption>{{ prettySize(totalSize) }}</q-item-label>
      <q-linear-progress :value="progress"></q-linear-progress>
    </q-item-section>
    <q-item-section side>
      <q-btn flat round icon="delete" @click="confirm = true"></q-btn>
    </q-item-section>
  </q-item>

    <q-dialog v-model="confirm" persistent>
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="delete" color="primary" text-color="white" />
          <span class="q-ml-sm">You are currently not connected to any network.</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="primary" v-close-popup />
          <q-btn flat label="Delete" color="primary" v-close-popup @click="deleteAction"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
</template>