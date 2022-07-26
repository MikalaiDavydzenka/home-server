<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import {useTransmission} from '@/stores/transmission';
import { onMounted } from 'vue'

const transmission = useTransmission();

onMounted(() => {
  // transmission.updateTorrentsList();

  let es = new EventSource('/cockpit/torrent');
  es.addEventListener('message', event => {
      let data = JSON.parse(event.data);
      transmission.torrents = data.torrents;
  }, false);

})
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
