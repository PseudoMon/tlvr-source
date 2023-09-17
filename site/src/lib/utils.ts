export async function loadJson<T>(dataurl: string): Promise<T> {
  const response = await fetch(dataurl);

  return response.json();
}

export interface LoadArgs {
  url: {
    origin: string
  }
}