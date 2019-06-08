Tundra (Simple4All project)
===

| Language  | ID | Corpus(Acoustic Model) | Phone set             | ok? | AM train? |   g2p my own?  | aligned-acc |
|-----------|----|------------------------|-----------------------|-----|-----------|----------------|------------ |
| Bulgarian | BG | GlobalPhone            | GlobalPhone           |  Y  |     X     |        X       |      Y      | 
| German    | DE | GlobalPhone            | GlobalPhone           |  Y  |     Y     |        X       |      Y      |
| English   | EN | LibriSpeech            | Arpabet  (stressed)   |  Y  |     X     |        X       |      Y      |
| Finnish   | FI | **Tundra**             | IPA                   |  Y  |     Y     |        Y       |      Y      |
| French    | FR | GlobalPhone            | GlobalPhone           |  Y  |     X     |        X       |      Y      |
| Hungarian | HU | **Tundra**             | IPA                   |  Y  |     Y     |        Y       |      Y      |
| Polish    | PL | GlobalPhone            | GlobalPhone           |  Y  |     X     |        X       |      Y      |
| Italian   | IT | **Tundra**             | CMU dict              |  Y  |     Y     |        Y       |      Y      |
| Romania   | RM | **Tundra**             | IPA                   |  Y  |     Y     |        Y       |      Y      |
| Dutch     | NL | **Tundra**             | CMU dict              |  Y  |     Y     |        Y       |      Y      |
| Portuguese| PT | GlobalPhone            | GlobalPhone           |  Y  |     X     |        X       |      Y      |
| Russian   | RU | GlobalPhone            | GlobalPhone           |  Y  |     X     |        X       |      Y      |

## Note
* ARPABET [ref](https://en.wikipedia.org/wiki/ARPABET)
* IARPA BABEL: If the words are in non-Latin script the locale used for sorting these UTF-8 files is by default `LANG=c`, unless there is a language-specific locale that is more appropriate. The lexicon entries must be identical to the transcription words. [ref](https://www.nist.gov/sites/default/files/documents/itl/iad/mig/IARPA_Babel_Specification-02062013.pdf)
