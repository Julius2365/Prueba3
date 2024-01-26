let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
        { orderable: false, targets: [5, 6] },
        { searchable: false, targets: [0, 5, 6] }
    ],
    pageLength: 4,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    dataTable = $("#datatable-libros").DataTable(dataTableOptions);
    await  listLibros();
    dataTableIsInitialized = true;
};

const itemElement = document.getElementById('idDelElementoQueContieneelID');
const listLibros = async () => {
    try {
        if(itemElement){
            const itemId =itemElement.dataset.itemId;
            const response = await fetch('http://127.0.0.1:8000/item/'+ itemId + '/')
        }else {
            console.error('Dato no encontrado')
        }

        console.log(response);
        const data = await response.json();
        let content = '';

        data.todolist_item.forEach((libro, index) => {
            content += `
                <tr>
                    <td>${index+1}</td>
                    <td>${libro.nombre}</td>
                    <td>${libro.precio}</td>
                    <td>${libro.autor}</td>
                    <td>${libro.score}</td>
                    <td>${libro.score >=8
                        ? "<i class='fa-solid fa-check' style='color: green;'></i>" 
                        : "<i class='fa-solid fa-xmark' style='color: red;'></i>"
                    }</td>
                </tr>`;
        });

        tableBody_libros.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener('load', async () => {
    await initDataTable();
});
