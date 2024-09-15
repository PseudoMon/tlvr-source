import { loadJson } from "$lib/utils";
import type { LoadArgs } from "$lib/utils";

interface CharVA {
  nameid: string,
  names: {
    en: string,
    cn: string,
    jp: string,
    kr: string,
  },
  actors: {
    en: {native: string, global: string},
    cn: {native: string, global: string},
    jp: {native: string, global: string},
    kr: {native: string, global: string},
  }
}

interface ReturnData {
  charlist: CharVA[],
}

export async function load({ url }: LoadArgs) {
  const dataurl = `${url.origin}/data/vadata-alt.json`;
  const charlist = await loadJson<CharVA[]>(dataurl);

  return {
    charlist
  }
}