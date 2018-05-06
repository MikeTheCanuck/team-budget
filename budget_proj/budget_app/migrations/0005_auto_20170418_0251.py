# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0004_lookupcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgethistory',
            name='accounting_object_name',
            field=models.CharField(default='', help_text='Full name of a general accounting category corresponding to an object_code, such as "Internal Material and Services".', max_length=255),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='amount',
            field=models.IntegerField(blank=True, help_text='Dollar amount as an integer, including 0. May be positive or negative.', null=True),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='bureau_code',
            field=models.CharField(default='', help_text='2-character ID for a Bureau, e.g. "PS" for Public Safety.', max_length=32),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='fiscal_year',
            field=models.CharField(default='', help_text='Fiscal Year as a string, e.g. 2015-16.', max_length=32),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='functional_area_code',
            field=models.CharField(default='', help_text='String ID for a functional area within a bureau, e.g. "PRREAQ" for Aquatics.', max_length=32),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='functional_area_name',
            field=models.CharField(default='', help_text='Name for a functional area corresponding to a functional_area_code within a bureau, e.g. "Aquatics".', max_length=255),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='fund_center_code',
            field=models.CharField(default='', help_text='String ID for a source of funds, e.g. "PKPR000025" for Aquatics Program Admin.', max_length=32),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='fund_center_name',
            field=models.CharField(default='', help_text='Name corresponding to a fund_center_code, e.g. "Systems Development Charges".', max_length=255),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='fund_code',
            field=models.CharField(default='', help_text='String ID [CAPITAL, DEBT_SVC, ENTERPRISE, GENERAL, INT_SVC, PERM, SPEC_REV, TRUST_PEN].', max_length=32),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='fund_name',
            field=models.CharField(default='', help_text='Name of a source of funds corresponding to a fund_code, e.g. "Capital Projects"', max_length=255),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='object_code',
            field=models.CharField(default='', help_text='Short string ID for a general accounting category, e.g. "EMS" for External Material and Services or "CAPITAL" for Capital Expenditures.', max_length=32),
        ),
        migrations.AlterField(
            model_name='budgethistory',
            name='service_area_code',
            field=models.CharField(default='', help_text='2-character ID [CD, EO, LA, PR, PS, PU, TP] for a Service Area, which is a grouping of related Bureaus.', max_length=32),
        ),
        migrations.AlterField(
            model_name='kpm',
            name='fy',
            field=models.CharField(default='', help_text='Fiscal year (i.e. 2015-16)', max_length=255),
        ),
        migrations.AlterField(
            model_name='ocrb',
            name='amount',
            field=models.IntegerField(blank=True, help_text='Integer dollar amount.', null=True),
        ),
        migrations.AlterField(
            model_name='ocrb',
            name='budget_category',
            field=models.CharField(default='', help_text='General category for this amount, which is one of [Capital, Operating].', max_length=255),
        ),
        migrations.AlterField(
            model_name='ocrb',
            name='budget_type',
            field=models.CharField(default='', help_text='Status of an item within the budget lifecycle: [Adopted, Revised, Actual].', max_length=255),
        ),
        migrations.AlterField(
            model_name='ocrb',
            name='fy',
            field=models.CharField(default='', help_text='Fiscal Year as a string, e.g. 2015-16', max_length=255),
        ),
        migrations.AlterField(
            model_name='ocrb',
            name='service_area',
            field=models.CharField(default='', help_text='Name of a Service Area, which is a grouping of related Bureaus.', max_length=255),
        ),
        migrations.AlterField(
            model_name='ocrb',
            name='source_document',
            field=models.CharField(default='', help_text='Reference to publicly available document from which this data was extracted.', max_length=255),
        ),
    ]