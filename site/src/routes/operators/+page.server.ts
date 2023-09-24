import { loadJson } from "$lib/utils";
import type { LoadArgs } from "$lib/utils";

interface ListLoadArgs extends LoadArgs {
  params: {
    charnameid: string
  }
}

interface SingleChar {
  nameid: string,
  numberid: string,
  name: {
    en: string,
    cn: string,
    jp: string,
    kr: string,
  },
}

interface ListData {
  charlist: SingleChar[]
}

export async function load({ url }: LoadArgs): Promise<ListData> {  
  const dataurl = `${url.origin}/data/charlist.json`;
  const chars = await loadJson<SingleChar[]>(dataurl);

  return {
    charlist: chars,
  }
}