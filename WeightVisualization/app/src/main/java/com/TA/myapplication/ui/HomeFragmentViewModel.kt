package com.TA.myapplication.ui

import androidx.lifecycle.ViewModel
import com.TA.myapplication.repository.DataRepository
import com.google.firebase.database.DatabaseReference

class HomeFragmentViewModel(private val dataRepository : DataRepository) : ViewModel(){

    fun getTheJson(path : String ) : DatabaseReference?{
        return dataRepository.getJsonFromDatabase(path)
    }
}