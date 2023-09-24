interface LoadArgs {
  url: {
    origin: string
  }
}

export async function load({ url }: LoadArgs) {
  const dataurl = `${url.origin}/data/welcome.json`;
  const response = await fetch(dataurl);

  return {
    welcomeText: response.json(),
  }
}