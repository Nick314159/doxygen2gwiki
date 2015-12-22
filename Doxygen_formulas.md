Doxygen allows you to put ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  formulas in the output (this works only for the HTML and ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  output, not for the RTF nor for the man page output). To be able to include formulas (as images) in the HTML documentation, you will also need to have the following tools installed
  * `latex:` the ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  compiler, needed to parse the formulas. To test I have used the teTeX 1.0 distribution.
  * `dvips:` a tool to convert DVI files to PostScript files I have used version 5.92b from Radical Eye software for testing.
  * `gs:` the GhostScript interpreter for converting PostScript files to bitmaps. I have used Aladdin GhostScript 8.0 for testing.


There are three ways to include formulas in the documentation.
  1. Using in-text formulas that appear in the running text. These formulas should be put between a pair of \f$ commands, so
```
  The distance between \f$(x_1,y_1)\f$ and \f$(x_2,y_2)\f$ is 
  \f$\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\f$.
```
results in:

The distance between ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_1.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_1.png)  and ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_2.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_2.png)  is ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_3.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_3.png) .
> 2. Unnumbered displayed formulas that are centered on a separate line. These formulas should be put between \f[and \f](.md) commands. An example:
```
  \f[
    |I_2|=\left| \int_{0}^T \psi(t) 
             \left\{ 
                u(a,t)-
                \int_{\gamma(t)}^a 
                \frac{d\theta}{k(\theta,t)}
                \int_{a}^\theta c(\xi)u_t(\xi,t)\,d\xi
             \right\} dt
          \right|
  \f]
```
results in: ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_4.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_4.png)
> 3. Formulas or other latex elements that are not in a math environment can be specified using \f{environment}, where `environment` is the name of the ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  environment, the corresponding end command is \f}. Here is an example for an equation array
```
   \f{eqnarray*}
        g &=& \frac{Gm_2}{r^2} \\ 
          &=& \frac{(6.673 \times 10^{-11}\,\mbox{m}^3\,\mbox{kg}^{-1}\,
              \mbox{s}^{-2})(5.9736 \times 10^{24}\,\mbox{kg})}{(6371.01\,\mbox{km})^2} \\ 
          &=& 9.82066032\,\mbox{m/s}^2
   \f}
```
which results in: ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_5.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_5.png)
For the first two commands one should make sure formulas contain valid commands in ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png) 's math-mode. For the third command the section should contain valid command for the specific environment.

Currently, doxygen is not very fault tolerant in recovering from typos in formulas. It may have to be necessary to remove the file `formula.repository` that is written to the html directory to a rid of an incorrect formula





---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|