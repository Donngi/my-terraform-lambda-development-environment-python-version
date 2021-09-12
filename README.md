# Example of development envirionment for terraform lambda (Runtime: Python)

## Deployment of lambda by terraform
The python package which will be uploaded to AWS Lambda must contain **all third patry libralies**.

However terraform doesn't have such function by default. So I complement missing function by using own shell script.

My deploy strategy is as follows.

1. zip src directory which doesn't contains third party packages.
2. If zip file is updated (= has another hash), execute shell script which makes package for upload that contains third-party libraries.
3. zip the package for upload.
4. If zip file is updated (= has another hash), update a lambda function.

The structure of lambda module (`module/lambda`) is as follows.

```
/module/lambda
├── lambda.tf
├── iam.tf
├── prepare_lambda_package.sh
├── src
└── upload
    ├── lambda.zip
    ├── lambda_without_third_party_packages.zip
    └── prepare
```

## Python development envirionment
| type | library |
| --- | --- | 
| Package management | pipenv |
| Formatter | black |
| Formatter (only import) | isort |
| Linter | flake8 |
| Type check | mypy |
| Test | pytest |
| Editor | VSCode |

The point is that **you have to place all config files at project root directory** as VSCode can only load these files at there.

To balance VSCode's GUI features and CLI command (`pipenv run foo`), I make a synbolic of config files in lambda src directory.


### VSCode setting
To enable all development tools stated above, you should add these settings to `settings.json`.

```json
{
    "python.languageServer": "Pylance",
    "python.autoComplete.extraPaths": [
        "./terraform/module/lambda/src",
    ],
    "python.analysis.extraPaths": [
        "./terraform/module/lambda/src",
    ],
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.flake8Enabled": false,
    "python.formatting.provider": "black",
    "python.linting.mypyEnabled": true,
    "python.linting.mypyArgs": [],
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```