# {{cookiecutter.project_slug}}
{% if cookiecutter.binder_integration == "TRUE" %}
JupyterLab: [![binder badge][binder_badge]][binder_lab]

RStudio: [![binder badge][binder_badge]][binder_studio]
{% endif %}
{{cookiecutter.project_short_description}}
{% if cookiecutter.binder_integration == "TRUE" %}
Integrated with binder: Click launch binder above to explore this project and run the code.
{% endif %}
Project Organization
--------------------

    .
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    ├── bin
{%- if cookiecutter.binder_integration == "TRUE" %}
    ├── binder
    │   ├── apt.txt
    │   ├── install.R
    │   ├── postBuild
    │   ├── requirements.txt
    │   └── runtime.txt{% endif %}
    ├── config
    ├── data
    │   ├── external
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── docs
    ├── notebooks
    ├── reports
    │   └── figures
    └── src
        ├── data
        ├── external
        ├── models
        ├── tools
        └── visualization
{% if cookiecutter.binder_integration == "TRUE" %}
<!-- Badges -->
[binder_badge]: https://mybinder.org/badge.svg
[binder_lab]: https://mybinder.org/v2/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/master?urlpath=lab
[binder_studio]: https://mybinder.org/v2/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/master?urlpath=rstudio{%- endif -%}
