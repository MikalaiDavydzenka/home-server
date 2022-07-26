<script setup lang="ts">
import TorrentsList from '@/components/TorrentsList.vue';
import TorrentAdd from '@/components/TorrentAdd.vue';
import {useTransmission} from '@/stores/transmission';
import { onMounted } from 'vue'

const transmission = useTransmission();

</script>

<template>
  <main>
    <TorrentAdd/>
    <TorrentsList :torrents-list="transmission.torrents"/>
  </main>
</template>
