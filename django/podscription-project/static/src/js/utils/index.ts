function formatDate(date) {
    const dayOfWeek = date.toLocaleString('default', { weekday: 'long' });
    const month = date.toLocaleString('default', { month: 'long' });
    const day = date.getDate();
    const year = date.getFullYear();
    return `${dayOfWeek} ${month} ${day}, ${year}`;
}

export { formatDate };