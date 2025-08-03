# 📝 Summarizer-App

A **Streamlit-based Text Summarization App** powered by Hugging Face's Transformers library. This app uses the `facebook/bart-large-cnn` model to generate concise summaries from long-form input text, making it easy to distill and understand large bodies of content.

---

## 🚀 Features

- ✅ **User-friendly web UI** built using Streamlit
- 🤖 **Summarization model**: `facebook/bart-large-cnn` via Hugging Face's `transformers` pipeline
- 🔐 **Secure API token** handling using `.env` and `python-dotenv`
- ✂️ **Automatic text chunking** for long documents
- ⚡ **Model caching** for faster response and efficiency
- 📋 **Formatted and readable summaries**

---

## 📂 File Structure
📁 Summarizer-App/

├── Summary2.py # Main Streamlit application

├── .env # Environment file to store Hugging Face API token

└── README.md # Project documentation (this file)

---

## Results 

![Screenshot 2025-06-30 225945](https://github.com/user-attachments/assets/3b8e562c-653d-4d6a-a8cb-04c3c5cd4d26)

## Input : 
"Why do fools fall in love? And when we do fall, why do our faculties of reason--and decency and self-respect and even right and wrong--sometimes not come along? For that matter, why would anyone reciprocate the love of a partner who has come so romantically unhinged?

The thought of a loved one can turn our wits upside down, ratchet up our heart rate, impel us to slay dragons and write corny songs. We may become morose, obsessive, even violent. Lovesickness has been blamed on the moon, on the devil, but whatever is behind it, it doesn't look like the behavior of a rational animal trying to survive and reproduce. But might there be a method to this amorous madness?

During the decades that the concept of human nature was taboo in academia, many scholars claimed that romantic love was a recent social construction. It was an invention of the Hallmark-card poets or Hollywood scriptwriters or, in one theory, medieval troubadours extolling the adulterous love of a knight for a lady.

For anyone who has been under love's spell, these theories seem preposterous, and so they are. Nothing so primal could have been created out of thin air as a mere custom or product. To the contrary, romantic love is a human universal. In 1896 a Kwakiutl Indian in southern Alaska wrote the lament "Fire runs through my body--the pain of loving you," which could be the title of a bad power ballad today. Similar outpourings of passion can be found all over the world from those with broken hearts.

Romantic infatuation is different from both raw lust and the enduring commitment that keeps lovers together long after their besottedness has faded. We all know the symptoms: idealized thoughts of the loved one; swings of mood from ecstasy to despair, insomnia and anorexia; and the intense need for signs of reciprocation. Even the brain chemistry is different: lust is fueled (in both sexes) by testosterone, and companionate love by vasopressin and oxytocin. Romantic passion taps the same dopamine system that is engaged by other obsessive drives like drug addiction.

For all this, there may be a paradoxical logic to romantic love. Imagine a world without it, a world of rational shoppers looking for the best available mate. Unsentimental social scientists and veterans of the singles scene know that this world is not entirely unlike our own. People shop for the most desirable person who will accept them, and that is why most marriages pair a bride and a groom of roughly equal desirability. The 10s marry the 10s, the 9s marry the 9s and so on. That is exactly what should happen in a marketplace where you want the best price you can get (the other person) for the goods you're offering (you).

But we also know this isn't the whole picture. Most daters find themselves at some point with a match who ought to be perfect but with whom for some reason the chemistry isn't there. Why do the principles of smart shopping give us only the rough statistics of mate choice, not the final pick?

The reason is that smart shopping isn't enough; both parties have to close the deal. Somewhere in this world lives the best-looking, richest, smartest person who would settle for you. But this ideal match is hard to find, and you may die single if you insist on waiting for such a mate to show up. So you choose to set up house with the best person you have found so far.

Your mate has gone through the same reasoning, which leaves you both vulnerable. The law of averages says that someday one of you will meet an even more desirable person; maybe a newly single Brad Pitt or Angelina Jolie will move in next door. If you are always going for the best you can get, at that point you will dump your partner pronto. But your partner would have invested time, child rearing and forgone opportunities in the relationship by that point. Anticipating this, your mate would have been foolish to enter the relationship in the first place, and the same is true for you. In this world of rational actors, neither of you could thus take the chance on the other. What could make you trust the other person enough to make that leap?

One answer is, Don't accept a partner who wanted you for rational reasons to begin with. Look for someone who is emotionally committed to you because you are you. If the emotion moving that person is not triggered by your objective mate value, that emotion will not be alienated by someone who comes along with greater mate value than yours. And there should be signals that the emotion is not faked, showing that the person's behavior is under the control of the involuntary parts of the brain--the ones in charge of heart rate, breathing, skin flushing and so on. Does this emotion sound familiar?

This explanation of infatuation was devised by the economist Robert Frank on the basis of the work of Nobel laureate Thomas Schelling. Social life is a series of promises, threats and bargains; in those games it sometimes pays to sacrifice your self-interest and control. An eco-protester who handcuffs himself to a tree guarantees that his threat to impede the logger is credible. The prospective home buyer who makes an unrecoverable deposit guarantees that her promise to buy the house is credible. And suitors who are uncontrollably smitten are in effect guaranteeing that their pledge of love is credible.

And this gets us to the dark side of romance. Threats, no less than promises, must be backed up by signs of commitment. A desperate lover in danger of being abandoned may resort to threatening his wife or girlfriend (yes, his; it's usually a man). The best way to prevent her from calling his bluff is in fact not to bluff--to be the kind of hothead who is crazy enough to do it. Of course, if he does make good on the threat, everyone loses (which is why the judicial system must make good on its threat to punish violent thugs).

This perverse logic of promises and threats lies behind the observation on romance offered by George Bernard Shaw: "When we want to read of the deeds that are done for love, whither do we turn? To the murder column."

Pinker is the Johnstone Professor of Psychology at Harvard University and the author, most recently, of The Stuff of Thought: Language as a Window into Human Nature"

## Output :
The thought of a loved one can turn our wits upside down. We may become morose, obsessive, even violent. Lovesickness has been blamed on the moon, on the devil. But might there be a method to this amorous madness? In 1896 a Kwakiutl Indian in southern Alaska wrote the lament "Fire runs through my body--the pain of loving you" Similar outpourings of passion can be found all over the world from those with broken hearts. Romantic passion taps the same dopamine system that is engaged by other obsessive drives. People shop for the most desirable person who will accept them. Most marriages pair a bride and a groom of roughly equal desirability. But we also know this isn't the whole picture. Most daters find themselves with a match who ought to be perfect but with whom for some reason the chemistry isn't there. The ideal match is hard to find, and you may die single if you insist on waiting for such a mate to show up. So you choose to set up house with the best person you have found so far. Your mate has gone through the same reasoning, which leaves you both vulnerable. Don't accept a partner who wanted you for rational reasons to begin with. Look for someone who is emotionally committed to you because you are you. Social life is a series of promises, threats and bargains. In those games it sometimes pays to sacrifice your self-interest and control. A desperate lover in danger of being abandoned may resort to threatening his wife or girlfriend. Threats, no less than promises, must be backed up by signs of commitment. buyer who makes an unrecoverable deposit guarantees that her promise to buy the house is credible. The writer is a professor of English at U.S. University and the author of several books on language and human nature. He is also the editor of The Stuff of Thought: Language as a Window into Human Nature. For more, go to www.thestuffofthought.com.


# Text Summarization Pro

![App Screenshot](https://via.placeholder.com/800x400?text=Text+Summarization+Pro+Screenshot)

An advanced NLP-powered text summarization application using Hugging Face's transformer models. This tool helps convert lengthy documents into concise, meaningful summaries with customizable output length.

## Table of Contents
- [Model Comparison](#model-comparison)
- [Key Improvements](#key-improvements)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

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
    subgraph Model 1 Flow
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
    
    subgraph Model 2 Flow
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
    
    style Model1 fill:#f9f,stroke:#333
    style Model2 fill:#bbf,stroke:#333
