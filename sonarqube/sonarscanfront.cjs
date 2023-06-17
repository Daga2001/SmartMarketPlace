const scanner = require('sonarqube-scanner');

scanner(
    {
        serverUrl: 'http://localhost:9000',
        token: "df72b7511a01d5ad94319c4ccbdc63c41b60cd3c",
        options: {
            'sonar.projectName': 'SmartMarketPlaceFront',
            'sonar.projectDescription': 'sonarqube smp-front',
            'sonar.projectKey': 'smp-front',
            'sonar.projectVersion': '0.0.1',
            'sonar.exclusions': 'node_modules/**, SmartMarketPlace_backend/**, .github/**',
            'sonar.projectBaseDir': '../',
            'sonar.login': 'admin',
            'sonar.password':'admin',
            'sonar.sourceEncoding': 'UTF-8',
        }
    },
    () => process.exit()
)