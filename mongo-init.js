db.createUser(
    {
        user: 'root-datagran',
        pwd: 'password-datagran',
        roles: [
            { role: "clusterMonitor", db: "admin" },
            { role: "dbOwner", db: "db_name" },
            { role: 'readWrite', db: 'db_datagran' }
        ]
    }
)