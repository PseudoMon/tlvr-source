interface LoadArgs {
  url: {
    origin: string
  }
}

export async function load({ url }: LoadArgs) {
  const dataurl = `${url.origin}/charlist.json`;
  const response = await fetch(dataurl);

  return {
    characters: response.json(),
  }
}