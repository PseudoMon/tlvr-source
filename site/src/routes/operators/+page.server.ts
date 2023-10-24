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

interface MiscData {
  nations: string[],
}

interface ReturnData {
  charlist: SingleChar[],
  miscdata: MiscData,
}

export async function load({ url }: LoadArgs): Promise<ReturnData> {  
  const dataurl = `${url.origin}/data/`;

  const charlist = await loadJson<SingleChar[]>(dataurl + "charlist.json");
  const miscdata = await loadJson<MiscData>(dataurl + "miscdata.json");

  return {
    charlist,
    miscdata,
  }
}