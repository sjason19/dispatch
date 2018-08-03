import React from 'react'

import { Position } from '@blueprintjs/core'

import { FormInput, TextInput, DateTimeInput, FileInput } from '../inputs'

export default function IssueForm(props) {
  return (
    <form onSubmit={e => e.preventDefault()}>
      <FormInput
        label='Article Headline'
        padded={false}
        error={props.errors.title}>
        <TextInput
          placeholder='Title'
          value={props.listItem.title || ''}
          fill={true}
          onChange={e => props.update('title', e.target.value)} />
      </FormInput>

      <FormInput
        label='File'
        padded={false}
        error={props.errors.file}>
        <FileInput
          placeholder={props.listItem.file_str || 'Choose a file...'}
          value={props.listItem.file || ''}
          fill={true}
          onChange={file => props.update('file', file)} />
      </FormInput>

      <FormInput
        label='Cover Image'
        padded={false}
        error={props.errors.img}>
        <FileInput
          placeholder={props.listItem.img_str || 'Choose a cover image...'}
          value={props.listItem.img || ''}
          fill={true}
          onChange={file => props.update('img', file)} />
      </FormInput>

      <FormInput
        label='Volume Number'
        padded={false}
        error={props.errors.volume}>
        <TextInput
          type='number'
          placeholder='Volume Number'
          value={props.listItem.volume || null}
          fill={true}
          onChange={e=> props.update('volume', e.target.value)} />
      </FormInput>

      <FormInput
        label='Issue Number'
        padded={false}
        error={props.errors.issue}>
        <TextInput
          type='number'
          placeholder='Issue Number'
          value={props.listItem.issue || null}
          fill={true}
          onChange={e=> props.update('issue', e.target.value)} />
      </FormInput>

      <FormInput
        label='Date'
        padded={false}
        error={props.errors.date}>
        <DateTimeInput
          value={props.listItem.date}
          position={Position.BOTTOM}
          showTimePicker={false}
          onChange={date => props.update('date', date)} />
      </FormInput>
    </form>
  )
}
