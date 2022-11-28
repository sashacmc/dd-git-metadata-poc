Generate
```bash
gradle init
```

Add the app/build.gradle
```xml
jar {
    manifest {
        attributes(
                'Main-Class': 'gitmetadatapoc.App'
        )
    }
}
```

Build
```bash
./gradlew build
```

Run
```bash
java -javaagent:../dd-java-agent.jar -Ddd.service=my-app -Ddd.env=staging -Ddd.version=1.0 -jar app/build/libs/app.jar
```
