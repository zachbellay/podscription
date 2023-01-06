function formatDate(date) {

    // assume that the date is a UTC date
    const newDate = new Date(date);
    console.log(newDate)

    const dayOfWeek = date.toLocaleString('default', { weekday: 'long', timeZone: 'UTC' });
    const month = date.toLocaleString('default', { month: 'long', timeZone: 'UTC' });
    const day = date.getDate({ timezone: 'UTC' });
    // console.log(date)
    // console.log(day)
    const year = date.getFullYear();
    return `${dayOfWeek} ${month} ${day}, ${year}`;
}

function formatSeconds(seconds) {
    // produces a string like 1h 30m 30s
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secondsLeft = Math.floor(seconds % 60);
    const hoursString = hours > 0 ? `${hours}h ` : '';
    const minutesString = minutes > 0 ? `${minutes}m ` : '';
    const secondsString = secondsLeft > 0 ? `${secondsLeft}s` : '';
    return `${hoursString}${minutesString}${secondsString}`;
}

function getBaseUrl() {
    const baseUrl = import.meta.env.MODE === 'development' ? 'http://localhost:8888' : 'https://podscription.app';
    return baseUrl;
}

export { formatDate, formatSeconds, getBaseUrl };