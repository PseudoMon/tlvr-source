import { loadJson } from "$lib/utils";
import type { LoadArgs } from "$lib/utils";

interface CharLoadArgs extends LoadArgs {
  params: {
    charnameid: string
  }
}

interface Chardata {
  nameid: string,
  names: {
    [key:string]: string,
  },
  actors: {
    [key:string]: {
      native: string,
      global: string,
    }
  }
}

export async function load({ url, params }: CharLoadArgs): Promise<Chardata> {
  const nameid = params.charnameid; 
  const dataurl = `${url.origin}/data/chardata/${nameid}.json`;
  const chardata = await loadJson<Chardata>(dataurl);

  return chardata;
}