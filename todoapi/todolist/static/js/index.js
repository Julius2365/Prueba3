let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3] },
        { orderable: false, targets: [3] },
        { searchable: false, targets: [0, 3] }
    ],
    pageLength: 4,
    destroy: true
};


const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    dataTable = $("#table-libros").DataTable({dataTableOptions});
    await listLibros();
    dataTableIsInitialized = true;
};

const itemElement = document.getElementById('index');
const tableBody_libros = document.getElementById('tableBody_libros');

const listLibros = async () => {
    try {
        if (itemElement) {
            const url = 'http://127.0.0.1:8000';
            console.log('Url de la solicitud',url);

            const  response = await fetch(url);

            if (response.ok) {
                const data = await response.json();
                let content = '';

                data.libros.forEach((libro, index) => {
                    content += `
                        <tr>
                            <td>${item.id - 10}</td>
                            <td>${libro.item.nombre}</td>
                            <td>${libro.item.autor}</td>
                            <td>${libro.item.precio}</td>
                            <td>${libro.score}</td>
                            <td>${libro.score >= 8
                                ? "<i class='fa-solid fa-check' style='color: green;'></i>"
                                : "<i class='fa-solid fa-xmark' style='color: red;'></i>"
                            }</td>
                        </tr>`;
                });

                tableBody_libros.innerHTML = content;
                dataTable.draw();
            } else {
                console.error('Error en la respuesta del servidor:', response.status);
            }
        }
    } catch (ex) {
        console.error('Error:', ex);
    }
};

window.addEventListener('load', async () => {
    console.log('Evento');
    await initDataTable();
});
