


export function getQueryParamValue(key: string, url: string, defaultValue: any): any {
    const urlParams = new URLSearchParams(url.slice(url.indexOf('?') + 1));
    return urlParams.get(key) ? urlParams.get(key) : defaultValue;
}

export function addOrModifyQueryParam(key: string, value: string, url: string): string {
    const urlParams = new URLSearchParams(url.slice(url.indexOf('?') + 1));
    // Check if the key exists, and modify its value if it does
    if (urlParams.has(key)) {
        urlParams.set(key, value);
    } else {
        // If the key doesn't exist, add a new key-value pair
        urlParams.append(key, value);
    }
    return `?${urlParams.toString()}`;
}