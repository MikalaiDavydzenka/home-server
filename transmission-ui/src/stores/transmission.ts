import { defineStore } from 'pinia'

export interface Torrent {
  id: number,
  name: string,
  progress: number,
  rateDownload: number,
  rateUpload: number,
  totalSize: number,
}

export const useTransmission = defineStore("transmission" , {
  state: () => ({
    torrents: Array<Torrent>()
  }),
  actions: {},
})
