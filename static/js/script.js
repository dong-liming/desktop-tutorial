document.getElementById('linkedListForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const operation = document.getElementById('operation').value;
    const position = document.getElementById('position')?.value;
    const value = document.getElementById('value')?.value;
    const deleteValue = document.getElementById('deleteValue')?.value;
    const specificPosition = document.getElementById('specificPosition')?.value;
    const data = {
        operation,
        position,
        value,
        deleteValue,
        specificPosition
    };
    axios.post('/linked_list_operation', data)
       .then(response => {
            document.getElementById('linkedListResult').textContent = response.data.result;
        })
       .catch(error => {
            console.error('Error:', error);
            document.getElementById('linkedListResult').textContent = 'An error occurred';
        });
});

document.getElementById('sortingForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const algorithm = document.getElementById('sortingAlgorithm').value;
    const size = document.getElementById('arraySize').value;
    const data = {
        algorithm,
        size
    };
    axios.post('/sorting_operation', data)
       .then(response => {
            document.getElementById('sortingResult').textContent = response.data.result;
        })
       .catch(error => {
            console.error('Error:', error);
            document.getElementById('sortingResult').textContent = 'An error occurred';
        });
});

document.getElementById('hashTableForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const type = document.getElementById('hashTableType').value;
    const operation = document.getElementById('hashTableOperation').value;
    const key = document.getElementById('hashTableKey')?.value;
    const data = {
        type,
        operation,
        key
    };
    axios.post('/hash_table_operation', data)
       .then(response => {
            document.getElementById('hashTableResult').textContent = response.data.result;
        })
       .catch(error => {
            console.error('Error:', error);
            document.getElementById('hashTableResult').textContent = 'An error occurred';
        });
});

document.getElementById('operation').addEventListener('change', function () {
    const operation = this.value;
    if (operation === 'insert') {
        document.getElementById('insertPositionGroup').classList.remove('hidden');
        document.getElementById('insertValueGroup').classList.remove('hidden');
        document.getElementById('deleteValueGroup').classList.add('hidden');
        document.getElementById('specificPositionGroup').classList.add('hidden');
    } else if (operation === 'delete') {
        document.getElementById('insertPositionGroup').classList.add('hidden');
        document.getElementById('insertValueGroup').classList.add('hidden');
        document.getElementById('deleteValueGroup').classList.remove('hidden');
        document.getElementById('specificPositionGroup').classList.add('hidden');
    } else {
        document.getElementById('insertPositionGroup').classList.add('hidden');
        document.getElementById('insertValueGroup').classList.add('hidden');
        document.getElementById('deleteValueGroup').classList.add('hidden');
        document.getElementById('specificPositionGroup').classList.add('hidden');
    }
    if (operation === 'insert' && document.getElementById('position').value ==='specific') {
        document.getElementById('specificPositionGroup').classList.remove('hidden');
    }
});

document.getElementById('hashTableOperation').addEventListener('change', function () {
    const operation = this.value;
    if (operation === 'insert' || operation ==='search' || operation === 'delete' || operation === 'access') {
        document.getElementById('hashTableKeyGroup').classList.remove('hidden');
    } else {
        document.getElementById('hashTableKeyGroup').classList.add('hidden');
    }
});