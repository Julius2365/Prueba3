const listLibros = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/');
        const data = await response.json();
        let content = '';

        data.Libros.forEach((libro, index) => {
            content += `
                <tr>
                    <td>${index}</td>
                    <td>${libro.precio}</td>
                    <td>${libro.autor}</td>
                </tr>
            `;
        });

        tableBody_todolist_item.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener('load', async () => {
    await listLibros();
});
