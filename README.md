# GitHub Petitions Regarding Removal of RMS: Contributor Comparison

On March 22, 2021 the former president of the Free Software Foundation (FSF) Richard M. Stallman (rms) announced that he would be returning to the FSF board.[^1] This comes 18 months after he stepped down, due to public pressure regarding, among other things, statements relating to the involvement of Marvin Minsky and Jeffrey Epstein.[^2]

On March 23, 2021 a letter was published online calling for the removal of rms from all leadership positions within the Free/Libre/Open Source Software community.[^3] Shortly thereafter, a counter letter, in support of the return of rms was published.[^4]

Each of these letters called for readers to add their signatures via a pull request (PR) using GitHub, one of the largest hosts for FLOSS projects. As of 10:00:00 UTC on March 25, 2021, the letter requesting removal has received over 2,000 signatures, while the letter in support of remaining has received just over 1,400.

Below is a cursory analysis comparing contributors to each letter. The data used was acquired from GitHub via thier official API, accessed using the PyGithub library.[^5] It was then processed in R, making use of tools from the tidyverse library.[^6]

The documentation provided for this project is released under a Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0) https://creativecommons.org/licenses/by-sa/4.0/. The code provided for this project is released under the GNU General Public License version 3 (GNU GPLv3) https://www.gnu.org/licenses/gpl-3.0. The data was collected from GitHub. All data provided for this project is subject to the terms outlined on this page: https://docs.github.com/en/github/site-policy/github-terms-of-service


[^1]: https://twitter.com/nixcraft/status/1373905399707955202
[^2]: https://itsfoss.com/richard-stallman-controversy
[^3]: https://rms-open-letter.github.io/
[^4]: https://rms-support-letter.github.io/
[^5]: https://github.com/PyGithub/PyGithub
[^6]: https://www.tidyverse.org/
