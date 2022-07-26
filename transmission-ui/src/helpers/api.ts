import { Buffer } from 'buffer'

async function postReq(url: string, data: object) {
    let resp = await fetch(
        url,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
    return resp;
}


async function deleteReq(url: string, data: object) {
    let resp = await fetch(
        url,
        {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
    return resp;
}


export async function addTorrent(file: File) {
    let arrayBuffer = await file.arrayBuffer();
    let buf = Buffer.from(arrayBuffer);
    let data = {
        "torrent": buf.toString("base64")
    };

    let resp = await postReq("cockpit/torrent", data);
    return resp;
}


export async function deleteTorrent(ids: Array<number>) {
    let data = {
        "torrentIds": ids,
    };

    let resp = await deleteReq("cockpit/torrent", data);
    return resp;
}
