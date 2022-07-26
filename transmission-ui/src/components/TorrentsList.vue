<script setup lang="ts">
import { prettySize } from "@/helpers/pretty"
import type { Torrent } from '@/stores/transmission';
import TorrentItem from "@/components/TorrentItem.vue"

defineProps<{
    torrentsList: Array<Torrent>
}>()
</script>

<template>
    List of torrents
    <div class="q-pa-md">
        <q-list v-for="item in torrentsList" bordered class="q-ma-md">
            <TorrentItem v-bind="item"/>
        </q-list>
    </div>
</template>