import {Story, Meta} from '@storybook/react/types-6-0';

import {SimpleCard, SimpleCardProps} from './SimpleCard';

export default {
    title: 'Components/Card',
    component: SimpleCard
} as Meta;

const Template: Story<SimpleCardProps> = (args) => <SimpleCard {...args} />

export const Default = Template.bind({});
Default.args = {
    header: 'Create Bill',
    description: `This will initiate the flow of bill creation where
    you\'ll enter the required information and share
    it with your clients either by mail, WhatsApp or
    simple PDF`,
    actionLink: '#',
    actionLabel: 'Click to get started'
}