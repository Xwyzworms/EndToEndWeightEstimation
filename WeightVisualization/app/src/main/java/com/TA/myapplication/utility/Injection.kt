package com.TA.myapplication.utility

import com.TA.myapplication.repository.DataRepository

object Injection {
    fun provideRepository() : DataRepository {
        return DataRepository.getInstance()
    }
}