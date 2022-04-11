package com.TA.myapplication.utility

import com.TA.myapplication.BuildConfig
import com.google.firebase.database.FirebaseDatabase

object Firebase {

    @Volatile
    private var instance : FirebaseDatabase ? = null

    fun getInstance() : FirebaseDatabase {
        return instance ?: synchronized(this) {
            val instanceTemp = FirebaseDatabase.getInstance(BuildConfig.DATABASE_URL)
            instance = instanceTemp
            instanceTemp
        }
    }
}