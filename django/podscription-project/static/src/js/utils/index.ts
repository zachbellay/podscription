function formatDate(date) {
    const dayOfWeek = date.toLocaleString('default', { weekday: 'long' });
    const month = date.toLocaleString('default', { month: 'long' });
    const day = date.getDate();
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

export { formatDate, formatSeconds };