package com.TA.myapplication.repository

import android.util.Log
import com.TA.myapplication.utility.Firebase
import com.google.firebase.database.DatabaseReference

class DataRepository ()
{

    private fun getTheDatabaseReference() : DatabaseReference{
        Log.d("HomeFragmenTCas",Firebase.getInstance().reference.toString())
        return Firebase.getInstance().reference
    }

    fun getJsonFromDatabase(path : String) : DatabaseReference? {
        try {
            return getTheDatabaseReference().child(path)
        } catch (e: Exception) {
            Log.d(TAG, " Error While Fetching data : ${e.message.toString()}")
        }
        return null
    }

    companion object {
        private val TAG : String = DataRepository::class.java.simpleName

        @Volatile
        private var INSTANCE : DataRepository? = null

        @JvmStatic
        fun getInstance() : DataRepository {
            return INSTANCE ?: synchronized(this) {
                val instance = DataRepository()
                INSTANCE = instance
                instance
            }
        }
    }
}
