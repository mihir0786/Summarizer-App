
# Text Summarization 

![App Screenshot](https://via.placeholder.com/800x400?text=Text+Summarization+Pro+Screenshot)

An advanced NLP-powered text summarization application using Hugging Face's transformer models. This tool helps convert lengthy documents into concise, meaningful summaries with customizable output length.

## Table of Contents
- [Model Comparison](#model-comparison)
- [Key Improvements](#key-improvements)
- [Architecture](#architecture)
- [Results](#Result)


## Model Comparison

| Feature                | Model 1 (BART)                          | Model 2 (FLAN-T5)                       |
|------------------------|----------------------------------------|----------------------------------------|
| **Base Model**         | facebook/bart-large-cnn                | google/flan-t5-large                   |
| **Task Type**          | summarization                          | text2text-generation                   |
| **Chunking Strategy**  | Word-based splitting                  | Paragraph-preserving smart chunking    |
| **Output Structure**   | Plain summary                         | Sectioned summary (Key Points, Details, Conclusions) |
| **UI Features**        | Basic input/output                    | Real-time stats, export options, progress tracking |
| **Error Handling**     | Basic                                 | Comprehensive with logging             |
| **Customization**      | Fixed summary length                  | 3-level length control                 |
| **Performance**        | Good for medium texts                 | Better for very long documents         |

## Key Improvements

From Model 1 to Model 2, we implemented:

1. **Enhanced Chunking Algorithm**:
   - Added paragraph-aware splitting
   - Fallback to word-based chunking when needed
   - Better context preservation

2. **Improved User Experience**:
   - Real-time text statistics
   - Progress indicators
   - Export options (TXT file, clipboard)
   - Session state management

3. **Advanced Features**:
   - Structured summary output
   - Multiple length presets
   - Comprehensive error logging
   - Processing time tracking

4. **Technical Upgrades**:
   - Better prompt engineering
   - Dynamic length adjustment per chunk
   - Caching improvements
   - Device management (CPU/GPU)

## Architecture

### Comparative Flowchart

```mermaid
graph TD
    subgraph Summary Model 1 Flow
        A1[Start] --> B1[Load BART Model]
        B1 --> C1[Input Text]
        C1 --> D1{Text > 1024?}
        D1 -->|Yes| E1[Split by Words]
        D1 -->|No| F1[Summarize Directly]
        E1 --> G1[Process Chunks]
        G1 --> H1[Combine Results]
        F1 --> I1[Display Summary]
        H1 --> I1
    end
    
    subgraph Summary Model 2 Flow
        A2[Start] --> B2[Load FLAN-T5]
        B2 --> C2[Input Text + Settings]
        C2 --> D2{Text > 1024?}
        D2 -->|Yes| E2[Smart Paragraph Chunking]
        D2 -->|No| F2[Process with Prompt]
        E2 --> G2[Process with Progress]
        G2 --> H2[Combine Structured Results]
        F2 --> I2[Display Enhanced Output]
        H2 --> I2
        I2 --> J2[Export Options]
    end

## Results
  
    
    
