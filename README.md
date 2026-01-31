# 🔄 Smart File Converter Hub

A powerful web-based file conversion tool built with Streamlit that supports multiple file format conversions.

## 🌟 Features

- **CSV → JSON**: Convert CSV files to JSON format
- **JSON → CSV**: Convert JSON files to CSV format
- **Excel → JSON**: Convert Excel files (.xlsx, .xls) to JSON
- **XML → JSON**: Convert XML files to JSON format
- **CSV → SQL**: Generate SQL INSERT statements from CSV files

## 🚀 Quick Start

### Local Development

1. **Clone or download the project**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open your browser**
- The app will automatically open at `http://localhost:8501`
- If not, navigate to the URL shown in your terminal

## 📦 Deployment to Streamlit Cloud (FREE)

### Step 1: Prepare Your Code
1. Create a GitHub repository
2. Upload these files:
   - `app.py`
   - `requirements.txt`
   - `README.md`

### Step 2: Deploy
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file path to `app.py`
6. Click "Deploy"

**Your app will be live in 2-3 minutes!** 🎉

### Alternative Deployment Options

#### Render (Free)
1. Go to [render.com](https://render.com)
2. Create new Web Service
3. Connect your GitHub repo
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

#### Heroku
1. Create `Procfile`:
```
web: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```
2. Deploy via Heroku CLI or GitHub integration

## 📁 Project Structure

```
smart-file-converter/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🛠️ Technical Stack

- **Framework**: Streamlit 1.29.0
- **Data Processing**: Pandas 2.1.4
- **Excel Support**: openpyxl 3.1.2
- **XML Parsing**: Python's built-in xml.etree.ElementTree
- **JSON Handling**: Python's built-in json module

## 📖 Usage Guide

### CSV to JSON
1. Select "CSV → JSON" from the sidebar
2. Upload your CSV file
3. Preview the JSON output
4. Download the converted file

### JSON to CSV
1. Select "JSON → CSV" from the sidebar
2. Upload your JSON file (must be an array of objects)
3. Preview the CSV output
4. Download the converted file

### Excel to JSON
1. Select "Excel → JSON" from the sidebar
2. Upload your Excel file (.xlsx or .xls)
3. Preview the JSON output
4. Download the converted file

### XML to JSON
1. Select "XML → JSON" from the sidebar
2. Upload your XML file
3. Preview the JSON output
4. Download the converted file

### CSV to SQL
1. Select "CSV → SQL" from the sidebar
2. Upload your CSV file
3. Enter your desired table name
4. Preview the SQL INSERT statements
5. Download the SQL file

## 🔧 Customization & Enhancement Ideas (Week 2+)

### Week 2 Enhancements:
- [ ] Add batch file conversion
- [ ] Support for more formats (PDF, DOCX, etc.)
- [ ] Add data validation before conversion
- [ ] Show preview of uploaded files
- [ ] Add conversion history

### Week 3 Enhancements:
- [ ] Add user authentication
- [ ] Store conversion history in database
- [ ] API endpoints for programmatic access
- [ ] Advanced SQL options (CREATE TABLE, indexes)
- [ ] Custom delimiter support for CSV

### Week 4 Enhancements:
- [ ] Add data transformation options
- [ ] Column mapping for conversions
- [ ] Scheduled conversions
- [ ] Email notifications
- [ ] Advanced error handling with logs

## 🐛 Troubleshooting

### Common Issues:

**Issue**: `ModuleNotFoundError: No module named 'streamlit'`
**Solution**: Run `pip install -r requirements.txt`

**Issue**: File upload fails
**Solution**: Check file size (Streamlit has 200MB default limit)

**Issue**: XML conversion errors
**Solution**: Ensure XML is well-formed and valid

**Issue**: JSON to CSV fails
**Solution**: Ensure JSON is an array of objects with consistent keys

## 📊 File Size Limits

- **Local Development**: Limited by system memory
- **Streamlit Cloud**: 200MB per file (default)
- **Custom Deployment**: Configure based on hosting plan

## 🔒 Security Notes

- Files are processed in-memory only
- No data is stored on servers
- All conversions happen client-side
- For production, consider adding:
  - File type validation
  - Virus scanning
  - Rate limiting
  - User authentication

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📧 Support

For issues or questions:
- Open an issue on GitHub
- Check Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)

## 🎯 Development Roadmap

**Phase 1 (Days 1-2)**: ✅ Core functionality
- All 5 conversion types
- Basic UI
- Deployment

**Phase 2 (Week 2)**: 🚧 Enhancements
- Better error handling
- File previews
- Batch processing

**Phase 3 (Week 3)**: 📋 Advanced Features
- API integration
- Database storage
- User accounts

**Phase 4 (Week 4+)**: 🚀 Production Ready
- Monitoring
- Analytics
- Performance optimization

## 🙏 Acknowledgments

Built with:
- [Streamlit](https://streamlit.io) - The fastest way to build data apps
- [Pandas](https://pandas.pydata.org) - Powerful data analysis library
- [openpyxl](https://openpyxl.readthedocs.io) - Excel file handling

---

**Made with ❤️ and ☕**

**Last Updated**: January 2026
