# task1
"Python Programming Internship Tasks - My Daily Work"
# 📝 To-Do List Application

A comprehensive task management application built with Python and Tkinter GUI framework. This application helps you organize your daily tasks with priority levels, completion tracking, and persistent data storage.

## ✨ Features

- **Task Management**: Add, edit, and delete tasks with ease
- **Priority Levels**: Organize tasks by High, Medium, or Low priority
- **Completion Tracking**: Mark tasks as complete with visual indicators
- **Persistent Storage**: Data is automatically saved to JSON file
- **Modern GUI**: Clean, intuitive interface with TreeView display
- **Task History**: Track when tasks were added with timestamps
- **Visual Indicators**: Color-coded priority levels and completion status

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- tkinter (usually comes with Python)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Gowthami398/task1.git
   cd task1
   ```

2. Run the application:
   ```bash
   python task1_todo_list.py
   ```

## ��️ Usage

### Adding Tasks
1. Enter your task in the text field
2. Select priority level (High, Medium, Low)
3. Click "Add Task" button

### Managing Tasks
- **Edit**: Double-click on any task to edit it
- **Delete**: Select a task and click "Delete Selected"
- **Complete**: Select a task and click "Mark Complete"

### Data Storage
- Tasks are automatically saved to `tasks.json`
- Data persists between application sessions
- No manual save required

## �� Project Structure
todo-list-app/
├── README.md
├── task1_todo_list.py
└── tasks.json (generated automatically)

## 🎨 UI Features

- **Dark Theme**: Professional dark color scheme
- **TreeView Display**: Organized task list with columns
- **Status Indicators**: Visual completion and priority markers
- **Responsive Design**: Adapts to different screen sizes
- **Error Handling**: User-friendly error messages

## 🔧 Technical Details

### Dependencies
- `tkinter` - GUI framework
- `json` - Data persistence
- `datetime` - Timestamp functionality

### Data Format
Tasks are stored in JSON format:
```json
{
  "text": "Task description",
  "priority": "High|Medium|Low",
  "completed": true|false,
  "date_added": "YYYY-MM-DD HH:MM"
}
```

## 🚀 Future Enhancements

- Task categories and tags
- Due date functionality
- Task search and filtering
- Export/import functionality
- Cloud synchronization
- Mobile app version

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 📞 Contact

For questions or support, please open an issue in this repository.

---

**Built with ❤️ using Python and Tkinter**
