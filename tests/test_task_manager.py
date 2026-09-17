from task_manager import TaskManager

def test_add_task():
    manager = TaskManager()
    manager.add_task("gym")
    assert manager.tasks[0].task == "gym"
    assert manager.tasks[0].id == 1
    manager.add_task("shopping")
    assert manager.tasks[1].task == "shopping"
    assert manager.tasks[1].id == 2
    assert manager.next_id == 3


def test_find_task():
    manager = TaskManager()
    manager.add_task("gym")
    manager.add_task("shopping")
    assert manager.find_task(1).task == "gym"
    assert manager.find_task(999) is None


def test_complete_task():
    manager = TaskManager()
    manager.add_task("gym")
    manager.add_task("shopping")
    assert manager.tasks[0].completed is False
    manager.complete_task(1)
    assert manager.tasks[0].completed is True


def test_complete_task_invalid_id():
    manager = TaskManager()
    manager.add_task("gym")
    manager.complete_task(999)
    assert manager.tasks[0].completed is False


def test_delete_task():
    manager = TaskManager()
    manager.add_task("gym")
    manager.add_task("shopping")
    manager.delete_task(1)
    assert len(manager.tasks) == 1
    assert manager.tasks[0].task == "shopping"


def test_delete_task_invalid_id():
    manager = TaskManager()
    manager.add_task("gym")
    manager.add_task("shopping")
    manager.delete_task(999)
    assert len(manager.tasks) == 2