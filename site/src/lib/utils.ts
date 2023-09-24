export async function loadJson<T>(dataurl: string): Promise<T> {
  const response = await fetch(dataurl);

  return response.json();
}

export interface LoadArgs {
  url: {
    origin: string
  }
}

export function getAvatarUrl(file: string, base: string): string {
  // Image from Aceship
  //`https://raw.githubusercontent.com/Aceship/Arknight-Images/main/avatars/${data.charid}.png` 

  // Image from local
  //`/images/avatars/${data.nameid}.webp` 

  return `${base}/images/avatars/${file}.webp` 
}