async function getTodoData(){
    const response = await fetch('/api/todos');
    return response.json();
}

function loadTable(todos){
    const table = document.querySelector('#result');
    for(let todo of todos){
        table.innerHTML += `<tr>
            <td>${todo.id}</td>
            <td>${todo.text}</td>
            <td>${todo.done}</td>
        </tr>`;
    }
}

async function main(){
    const todos = await getTodoData();
    loadTable(todos);
}

main();