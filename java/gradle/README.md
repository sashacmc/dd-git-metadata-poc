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
java -jar ./app/build/libs/app.jar
```
