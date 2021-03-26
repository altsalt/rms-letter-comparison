# GitHub Petitions Regarding Removal of RMS: Contributor Comparison

## How to use
0. `git clone https://github.com/altsalt/rms-letter-comparison.git`
1. `cd rms-letter-comparison`
2. `source ./gh_credentials`
3. `python3 ./code/00-gather_data.py`
  - To view progress, consider running the following command:
  - `watch -d -n 30 "wc -l ./data/rms-letter-signers.csv && tail write.log && tail rate.log && tail error.log"`
4. Open `./code/01-process_data.R`, `./code/02-build_tables.R`, and `./rms-letter-comparison.Rmd` in RStudio
5. Run each RScript in sequence, they will read in the raw data, process it, save it to Rds files, and produce the PDF, `./rms-letter-comparison.pdf`

## Background and Setting
On March 22, 2021 the former president of the Free Software Foundation (FSF) Richard M. Stallman (rms) announced that he would be returning to the FSF board.<sup>[1](#fn1)</sup> This comes 18 months after he stepped down, due to public pressure regarding, among other things, statements relating to the involvement of Marvin Minsky and Jeffrey Epstein.<sup>[2](#fn2)</sup>

On March 23, 2021 a letter was published online calling for the removal of rms from all leadership positions within the Free/Libre/Open Source Software community.<sup>[3](#fn3)</sup> Shortly thereafter, a counter letter, in support of the return of rms was published.<sup>[4](#fn4)</sup>

Each of these letters called for readers to add their signatures via a pull request (PR) using GitHub, one of the largest hosts for FLOSS projects. As of 10:00:00 UTC on March 25, 2021, the letter requesting removal has received over 2,000 signatures, while the letter in support of remaining has received just over 1,400.

Included in this repository is a cursory analysis comparing contributors to each letter. The data used was acquired from GitHub via thier official API, accessed using the PyGithub library.<sup>[5](#fn5)</sup> It was then processed in R, making use of tools from the tidyverse library.<sup>[6](#fn6)</sup>

- <a name="fn1">[1]</a>: https://twitter.com/nixcraft/status/1373905399707955202
- <a name="fn2">[2]</a>: https://itsfoss.com/richard-stallman-controversy
- <a name="fn3">[3]</a>: https://rms-open-letter.github.io/
- <a name="fn4">[4]</a>: https://rms-support-letter.github.io/
- <a name="fn5">[5]</a>: https://github.com/PyGithub/PyGithub
- <a name="fn6">[6]</a>: https://www.tidyverse.org/

### Organizational messages regarding the current events:
- [CommitChange](https://twitter.com/wwahammy/status/1374771022289854465)
- [Electronic Frontier Foundation (EFF)](https://www.eff.org/deeplinks/2021/03/statement-re-election-richard-stallman-fsf-board)
- [Free Software Foundation Europe (FSFE)](https://fsfe.org/news/2021/news-20210324-01.html)
- [Mozilla](https://twitter.com/mozilla/status/1374513444838199304)
- [Open Source Initiative (OSI)](https://opensource.org/OSI_Response)
- [Outreachy](https://www.outreachy.org/blog/2021-03-23/fsf-participation-barred/)
- [Red Hat](https://www.redhat.com/en/blog/red-hat-statement-about-richard-stallmans-return-free-software-foundation-board)
- [Software Freedom Conservancy](https://sfconservancy.org/blog/2021/mar/23/outreachy-fsf/)
- [The Tor Project](https://twitter.com/torproject/status/1374754834050654212)

## Licensing and Usage Terms
The documentation provided for this project is released under a Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0) https://creativecommons.org/licenses/by-sa/4.0/. The code provided for this project is released under the GNU General Public License version 3 (GNU GPLv3) https://www.gnu.org/licenses/gpl-3.0. The data was collected from GitHub. All data provided for this project is subject to the terms outlined on this page: https://docs.github.com/en/github/site-policy/github-terms-of-service

🄯 2021 Wm Salt Hale <@altsalt (.net)>
