const scanner = require('sonarqube-scanner');

scanner(
    {
        serverUrl: 'http://localhost:9000',
        token: "db7ec434bc63bd11a011420a15ca51577e9549fb",
        options: {
            'sonar.projectName': 'SmartMarketPlaceBack',
            'sonar.projectDescription': 'sonarqube smp-back',
            'sonar.projectKey': 'smp-back',
            'sonar.projectVersion': '0.0.1',
            'sonar.exclusions': 'node_modules/**, public/**, src/**',
            'sonar.projectBaseDir': '../',
            'sonar.login': 'admin',
            'sonar.password':'admin',
            'sonar.sourceEncoding': 'UTF-8',
        }
    },
    () => process.exit()
)